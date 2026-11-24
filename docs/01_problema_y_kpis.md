# Problema y KPIs  (módulo 02)

## Tema

Autenticación de billetes: detectar automáticamente si un billete es auténtico o falso a partir de características extraídas de su imagen.

## Dataset

- **Fuente:** UCI Machine Learning Repository, *Banknote Authentication* (https://archive.ics.uci.edu/dataset/267/banknote+authentication)
- **Fecha de descarga:** 2026-11-21
- **Tamaño:** 1372 filas × 5 columnas (46 KB)
- **Qué representa una fila:** un billete fotografiado. Las imágenes se procesaron con una transformada wavelet y de ahí salen 4 características numéricas.
- **Columnas (el archivo no trae encabezados):**

| # | Nombre propuesto | Descripción |
|---|---|---|
| 1 | `variance` | Varianza de la imagen transformada |
| 2 | `skewness` | Asimetría de la imagen transformada |
| 3 | `curtosis` | Curtosis de la imagen transformada |
| 4 | `entropy` | Entropía de la imagen |
| 5 | `class` | 0 = auténtico, 1 = falso |

- **Balance de clases:** 762 auténticos (55,5 %) y 610 falsos (44,5 %).

## ¿Quién decide y qué decisión?

Quien opera un cajero automático, una máquina de conteo o una caja de un comercio decide si **acepta o rechaza** un billete. Rechazar uno bueno molesta al cliente. Aceptar uno falso es una pérdida directa de dinero y un problema legal.

## Preguntas por tipo de análisis

| Tipo | Pregunta |
|---|---|
| Descriptivo | ¿Cómo se distribuyen las 4 características en cada clase? ¿Hay valores atípicos? |
| Diagnóstico | ¿Qué características separan mejor los billetes falsos de los auténticos? ¿Por qué se confunden algunos? |
| Predictivo | Dadas las 4 características de un billete nuevo, ¿es falso o auténtico, y con qué probabilidad? |
| Prescriptivo | ¿Qué umbral de probabilidad conviene usar para rechazar un billete, dado que aceptar uno falso cuesta más que rechazar uno bueno? |

## KPIs SMART

| KPI | Fórmula | Meta | Periodo | Columnas |
|---|---|---|---|---|
| Recall de billetes falsos | falsos detectados / falsos totales | ≥ 0,99 | Conjunto de prueba | `class` y predicción |
| Precisión sobre los rechazos | falsos reales / billetes rechazados | ≥ 0,97 | Conjunto de prueba | `class` y predicción |
| Tasa de rechazo de billetes buenos | auténticos rechazados / auténticos totales | ≤ 0,02 | Conjunto de prueba | `class` y predicción |
| Mejora sobre el *baseline* | métrica del modelo − métrica de predecir siempre la clase mayoritaria | Superar claramente al *baseline* (exactitud 55,5 %) | Conjunto de prueba | `class` |

> Las metas son hipótesis iniciales. Se ajustan después del EDA y del baseline.
