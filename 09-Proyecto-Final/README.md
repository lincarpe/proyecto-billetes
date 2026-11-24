# 09 · Proyecto final

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué incluye la entrega

| Parte | Dónde |
|---|---|
| Problema, equipo, dataset, cómo ejecutar, resultados y límites | [`README.md`](../README.md) |
| Documentos por etapa | [`docs/`](../docs/) |
| Código reutilizable (limpieza, pipeline, entrenamiento) | [`src/`](../src/) |
| Notebooks de EDA y modelado | [`notebooks/`](../notebooks/) |
| API y pruebas | [`api/`](../api/) y [`tests/`](../tests/) |
| Entorno reproducible | [`pyproject.toml`](../pyproject.toml) y [`uv.lock`](../uv.lock) |

## Reproducir el proyecto desde cero

```bash
uv sync
uv run python -m src.limpieza
uv run python -m src.train
uv run uvicorn api.main:app
```

## Límites que conviene decir

- El proyecto lo hizo una sola persona, así que hay un solo autor en el historial y no hay pull requests de revisión.
- El resultado de 100 % en test (270 billetes) no significa que el modelo sea perfecto.
- No se sabe cómo se comportaría con otros billetes, otras cámaras u otra iluminación.

## Estado

La entrega final está pendiente.
