"""API para autenticar billetes.

Ejecutar:  uv run uvicorn api.main:app --reload
Documentación interactiva: http://127.0.0.1:8000/docs
"""

from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.limpieza import FEATURES

RUTA_MODELO = Path(__file__).resolve().parent.parent / "models" / "modelo.joblib"
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


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "modelo_cargado": estado["modelo"] is not None}


@app.post("/predict", response_model=Prediccion)
def predict(billete: Billete) -> Prediccion:
    modelo = estado["modelo"]
    if modelo is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo no disponible. Entrénalo con: uv run python -m src.train",
        )
    X = pd.DataFrame([billete.model_dump()])[FEATURES]
    prob_falso = float(modelo.predict_proba(X)[0, 1])
    es_falso = prob_falso >= UMBRAL
    return Prediccion(
        clase=int(es_falso),
        etiqueta="falso" if es_falso else "auténtico",
        probabilidad_falso=round(prob_falso, 4),
        accion="rechazar" if es_falso else "aceptar",
    )
