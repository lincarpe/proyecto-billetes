# 05 · EDA

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

Se exploraron las 4 variables y su relación con la clase, sobre los datos limpios (1348 filas).

## Hallazgos principales

1. `variance` es la variable que mejor separa las clases: media 2,36 en auténticos y −1,87 en falsos, con correlación de −0,74 con la clase.
2. `skewness` también ayuda (−0,45). `curtosis` (0,15) y `entropy` (−0,03) aportan poco por sí solas.
3. Con `variance` y `skewness` las clases forman dos nubes casi separables, así que se esperan métricas muy altas.
4. Hay valores atípicos solo en `curtosis` (59) y `entropy` (32). Se conservan.

## Dónde está

| Qué | Dónde |
|---|---|
| Notebook del análisis | [`notebooks/05_eda.ipynb`](../notebooks/05_eda.ipynb) |
| Hallazgos e hipótesis del charter | [`docs/04_eda.md`](../docs/04_eda.md) |
