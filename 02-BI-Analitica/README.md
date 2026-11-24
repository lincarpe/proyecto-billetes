# 02 · BI y analítica: problema y KPIs

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

Se definió el problema de negocio, quién decide y cuáles son los KPIs, antes de modelar.

- **Tema:** detectar si un billete es auténtico o falso a partir de 4 características de su imagen.
- **Quién decide:** quien opera un cajero, una máquina de conteo o una caja decide si acepta o rechaza el billete. Aceptar uno falso cuesta más que rechazar uno bueno.
- **Dataset:** Banknote Authentication (UCI), 1372 filas × 5 columnas.

## KPIs

| KPI | Meta |
|---|---|
| Recall de billetes falsos | ≥ 0,99 |
| Precisión sobre los rechazos | ≥ 0,97 |
| Tasa de rechazo de billetes buenos | ≤ 0,02 |
| Mejora sobre el baseline | Superar la exactitud de 55,5 % de predecir siempre "auténtico" |

## Dónde está

| Qué | Dónde |
|---|---|
| Problema, preguntas por tipo de análisis y KPIs | [`docs/01_problema_y_kpis.md`](../docs/01_problema_y_kpis.md) |
