"""API para autenticar billetes.

Ejecutar:  uv run uvicorn api.main:app --reload
Documentación interactiva: http://127.0.0.1:8000/docs
"""

import json
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

from src.limpieza import FEATURES

RUTA_MODELO = Path(__file__).resolve().parent.parent / "models" / "modelo.joblib"
RUTA_METRICAS = RUTA_MODELO.parent / "metricas.json"
MAX_LOTE = 100  # máximo de billetes por solicitud en /predict/batch
UMBRAL = 0.5  # probabilidad de "falso" a partir de la cual se rechaza el billete

estado: dict = {"modelo": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Carga el modelo al arrancar. Si no existe, la API arranca pero /predict responde 503."""
    estado["modelo"] = joblib.load(RUTA_MODELO) if RUTA_MODELO.exists() else None
    yield
    estado["modelo"] = None


app = FastAPI(
    title="Autenticación de billetes",
    description="Clasifica un billete como auténtico o falso a partir de 4 características de su imagen.",
    version="0.1.0",
    lifespan=lifespan,
)


class Billete(BaseModel):
    variance: float = Field(description="Varianza de la imagen transformada (wavelet)", examples=[3.62])
    skewness: float = Field(description="Asimetría de la imagen transformada", examples=[8.67])
    curtosis: float = Field(description="Curtosis de la imagen transformada", examples=[-2.81])
    entropy: float = Field(description="Entropía de la imagen", examples=[-0.45])


class Prediccion(BaseModel):
    clase: int = Field(description="0 = auténtico, 1 = falso")
    etiqueta: str
    probabilidad_falso: float = Field(ge=0, le=1)
    accion: str = Field(description="Aceptar o rechazar el billete")


@app.get("/", include_in_schema=False)
def inicio() -> RedirectResponse:
    """La raíz lleva a la documentación interactiva."""
    return RedirectResponse(url="/docs")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "modelo_cargado": estado["modelo"] is not None}


def _predecir(modelo, billetes: list[Billete]) -> list[Prediccion]:
    X = pd.DataFrame([b.model_dump() for b in billetes])[FEATURES]
    probs = modelo.predict_proba(X)[:, 1]
    resultado = []
    for p in probs:
        es_falso = float(p) >= UMBRAL
        resultado.append(
            Prediccion(
                clase=int(es_falso),
                etiqueta="falso" if es_falso else "auténtico",
                probabilidad_falso=round(float(p), 4),
                accion="rechazar" if es_falso else "aceptar",
            )
        )
    return resultado


def _modelo_o_503():
    if estado["modelo"] is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo no disponible. Entrénalo con: uv run python -m src.train",
        )
    return estado["modelo"]


@app.get("/model-info")
def model_info() -> dict:
    """Metadata del modelo entrenado: cuál es, con qué semilla y qué métricas obtuvo en test."""
    _modelo_o_503()
    return json.loads(RUTA_METRICAS.read_text(encoding="utf-8"))


@app.post("/predict", response_model=Prediccion)
def predict(billete: Billete) -> Prediccion:
    return _predecir(_modelo_o_503(), [billete])[0]


@app.post("/predict/batch", response_model=list[Prediccion])
def predict_batch(billetes: list[Billete]) -> list[Prediccion]:
    """Clasifica varios billetes en una sola solicitud (máximo 100)."""
    modelo = _modelo_o_503()
    if not billetes:
        raise HTTPException(status_code=422, detail="El lote no puede estar vacío.")
    if len(billetes) > MAX_LOTE:
        raise HTTPException(status_code=400, detail=f"El lote supera el máximo de {MAX_LOTE} billetes.")
    return _predecir(modelo, billetes)
