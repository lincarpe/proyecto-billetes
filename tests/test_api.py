"""Pruebas de la API. Si el modelo no existe, lo entrena antes de empezar."""

import pytest
from fastapi.testclient import TestClient

from api.main import RUTA_MODELO, app

# Billetes tomados del dataset original (primera fila de cada clase).
AUTENTICO = {"variance": 3.6216, "skewness": 8.6661, "curtosis": -2.8073, "entropy": -0.44699}
FALSO = {"variance": -1.3971, "skewness": 3.3191, "curtosis": -1.3927, "entropy": -1.9948}


@pytest.fixture(scope="module")
def client():
    if not RUTA_MODELO.exists():
        from src.train import main

        main()
    with TestClient(app) as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok", "modelo_cargado": True}


def test_predict_autentico(client):
    r = client.post("/predict", json=AUTENTICO)
    assert r.status_code == 200
    cuerpo = r.json()
    assert cuerpo["clase"] == 0
    assert cuerpo["accion"] == "aceptar"
    assert cuerpo["probabilidad_falso"] < 0.5


def test_predict_falso(client):
    r = client.post("/predict", json=FALSO)
    assert r.status_code == 200
    cuerpo = r.json()
    assert cuerpo["clase"] == 1
    assert cuerpo["accion"] == "rechazar"
    assert cuerpo["probabilidad_falso"] >= 0.5


def test_predict_falta_un_campo(client):
    incompleto = {k: v for k, v in AUTENTICO.items() if k != "entropy"}
    assert client.post("/predict", json=incompleto).status_code == 422


def test_predict_tipo_invalido(client):
    assert client.post("/predict", json={**AUTENTICO, "variance": "abc"}).status_code == 422


def test_predict_sin_modelo_devuelve_503():
    from api import main

    guardado = main.estado["modelo"]
    main.estado["modelo"] = None
    try:
        # Sin "with" no corre el lifespan, así que el modelo sigue en None.
        r = TestClient(app).post("/predict", json=AUTENTICO)
    finally:
        main.estado["modelo"] = guardado
    assert r.status_code == 503


def test_predict_batch(client):
    r = client.post("/predict/batch", json=[AUTENTICO, FALSO])
    assert r.status_code == 200
    assert [p["clase"] for p in r.json()] == [0, 1]


def test_predict_batch_demasiado_grande(client):
    assert client.post("/predict/batch", json=[AUTENTICO] * 101).status_code == 400


def test_predict_batch_vacio(client):
    assert client.post("/predict/batch", json=[]).status_code == 422


def test_model_info(client):
    r = client.get("/model-info")
    assert r.status_code == 200
    assert r.json()["modelo_elegido"] == "svm_rbf"
