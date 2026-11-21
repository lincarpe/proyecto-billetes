# Autenticación de billetes falsos

> Clasificar si un billete es auténtico o falso a partir de características extraídas de su imagen.

## Equipo

| Integrante | Rol principal | GitHub |
|---|---|---|
| TU NOMBRE (equipo de una persona) | Datos, EDA, modelado y API | @lincarpe |

## Problema de negocio

_(se completa en el módulo 02)_

## Dataset

- **Nombre:** Banknote Authentication
- **Fuente:** UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/267/banknote+authentication
- **Tamaño:** 1372 filas × 5 columnas (46 KB)
- **Variables:** 4 numéricas extraídas de imágenes de billetes (varianza, asimetría, curtosis y entropía de la transformada wavelet) y la clase.
- **Variable objetivo:** clase (0 = auténtico, 1 = falso)
- **Ubicación:** `data/raw/banknote/data_banknote_authentication.txt` (sin encabezados)

## Cómo ejecutar

```bash
uv sync
uv run jupyter lab
```

## Estructura

```
├── data/raw/          ← datos originales
├── data/processed/    ← datos limpios (generados)
├── docs/              ← problema, charter, decisiones
├── notebooks/         ← exploración
├── src/               ← código reutilizable (limpieza, train, api)
└── models/            ← modelos entrenados (generados)
```

## Avance

- [ ] 00 Entorno con uv
- [ ] 01 Repositorio en GitHub
- [ ] 02 Problema y KPIs
- [ ] 03 Project charter
- [ ] 04 Limpieza
- [ ] 05 EDA
- [ ] 06 Baseline
- [ ] 07 Pipeline de entrenamiento
- [ ] 08 API
- [ ] 09 Entrega final
