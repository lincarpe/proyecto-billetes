# 03 · CRISP-DM: project charter

> Esta carpeta es un índice. El código y los documentos viven en `src/`, `api/`, `notebooks/` y `docs/`.

## Qué se hizo

Se escribió el project charter, de una página, con el contexto, el objetivo, los criterios de éxito, el alcance y los riesgos.

- **Tipo de problema:** clasificación binaria. La variable objetivo es `class` (0 = auténtico, 1 = falso).
- **Criterios de éxito:** recall de falsos ≥ 0,99 y tasa de rechazo de billetes buenos ≤ 2 %.
- **Alcance:** limpieza, EDA, baseline, comparación de modelos, pipeline reproducible y una API. No incluye procesar imágenes ni desplegar en producción.
- **Riesgos principales:** resultados casi perfectos que parecen sospechosos, dataset pequeño, duplicados y fuga de información (*data leakage*).

## Dónde está

| Qué | Dónde |
|---|---|
| Project charter | [`docs/02_project_charter.md`](../docs/02_project_charter.md) |
