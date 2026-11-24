# 04 · Preparación de datos

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

Se limpiaron los datos con un script reutilizable y se documentó cada decisión.

| Decisión | Resultado |
|---|---|
| El archivo no trae encabezados | Se asignaron los nombres `variance`, `skewness`, `curtosis`, `entropy` y `class` |
| Valores nulos | No hay, no se imputó nada |
| Filas duplicadas exactas | Se eliminaron 24, para que una misma fila no caiga en entrenamiento y en prueba |
| Valores atípicos | Se conservan, son mediciones reales |

**Resultado:** de 1372 filas quedaron 1348 (738 auténticos y 610 falsos).

## Dónde está

| Qué | Dónde |
|---|---|
| Código de limpieza | [`src/limpieza.py`](../src/limpieza.py) |
| Decisiones de limpieza | [`docs/03_decisiones_limpieza.md`](../docs/03_decisiones_limpieza.md) |
| Datos originales | [`data/raw/banknote/`](../data/raw/banknote/) |

## Cómo ejecutarlo

```bash
uv run python -m src.limpieza   # genera data/processed/billetes_limpio.csv
```
