# Decisiones de limpieza (módulo 04)

Código: `src/limpieza.py`. Se ejecuta con `uv run python -m src.limpieza`.

| # | Problema encontrado | Decisión | Justificación | Filas afectadas |
|---|---|---|---|---|
| 1 | El archivo no trae encabezados | Asignar nombres: `variance`, `skewness`, `curtosis`, `entropy`, `class` | Son los nombres documentados por UCI | — |
| 2 | Valores nulos | No hay: no se imputa nada | Se verificó con `isna().sum()` (0 nulos) | 0 |
| 3 | Filas duplicadas exactas | Eliminarlas | Con duplicados, una misma fila podría caer en entrenamiento y en prueba y inflar las métricas (*data leakage*). Los 24 duplicados son de la clase 0 y ninguno tiene la misma combinación de variables con otra clase, así que no hay contradicciones | 24 |
| 4 | Valores atípicos | No se eliminan | Son mediciones reales de imágenes y los modelos que se van a usar no son sensibles a ellos. Se documentan en el EDA | 0 |
| 5 | Tipos de datos | Sin cambios | Las 4 variables ya son `float` y la clase `int` | 0 |

## Resultado

- Antes: 1372 filas (762 auténticos, 610 falsos).
- Después: **1348 filas (738 auténticos, 610 falsos)**.
- Proporción de la clase falso: 45,3 %. Se considera balanceado, así que no hace falta remuestreo.
- Salida: `data/processed/billetes_limpio.csv` (no se sube a Git, se regenera con el script).
