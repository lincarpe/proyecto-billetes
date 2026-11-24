# 00 · Entornos con uv

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

El proyecto usa `uv` para crear el entorno virtual, instalar las librerías y ejecutar los comandos. Con eso funciona igual en cualquier computador.

## Dónde está

| Qué | Dónde |
|---|---|
| Dependencias y versión de Python (>= 3.14) | [`pyproject.toml`](../pyproject.toml) |
| Versiones exactas de cada librería | [`uv.lock`](../uv.lock) |
| Guía paso a paso del entorno | [`docs/00_entorno_uv.md`](../docs/00_entorno_uv.md) |

## Comandos principales

```bash
uv sync                      # crea el entorno e instala todo
uv run python -m src.train   # ejecuta un comando dentro del entorno
```
