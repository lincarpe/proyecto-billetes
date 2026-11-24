# 08 · API con FastAPI

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

Se publicó el modelo como una API REST. Recibe las 4 medidas de un billete y responde si es auténtico o falso, con la probabilidad y la acción a tomar (aceptar o rechazar). Los datos de entrada se validan con Pydantic.

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/health` | Estado de la API y si el modelo está cargado |
| GET | `/model-info` | Qué modelo se usa y qué métricas obtuvo en test |
| POST | `/predict` | Clasifica un billete |
| POST | `/predict/batch` | Clasifica hasta 100 billetes en una solicitud |

Si el modelo no está entrenado, la API responde 503. Si falta un campo o el tipo es inválido, responde 422.

## Dónde está

| Qué | Dónde |
|---|---|
| Código de la API | [`api/main.py`](../api/main.py) |
| Pruebas (11) | [`tests/test_api.py`](../tests/test_api.py) |
| Tabla de rutas y ejemplo con `curl` | [`README.md`](../README.md#api) |

## Cómo ejecutarlo

```bash
uv run python -m src.train        # genera el modelo (una sola vez)
uv run uvicorn api.main:app       # abre http://127.0.0.1:8000/docs
uv run pytest                     # pruebas
```
