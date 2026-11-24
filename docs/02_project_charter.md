# Project Charter: Autenticación de billetes falsos

> Documento de **una página** que alinea al equipo y a los *stakeholders*. Se actualiza en cada iteración de CRISP-DM.

**Equipo:** Lina Marcela Carvajal Perez (@lincarpe, equipo de una persona) · **Fecha:** 2026-11-21 · **Versión:** 0.1

## 1. Contexto y problema de negocio

Los billetes falsos que pasan por cajeros, máquinas de conteo y cajas de comercios generan pérdidas directas y problemas legales. Revisarlos a mano es lento y depende de la experiencia de la persona. Se necesita un clasificador que, a partir de características medidas en la imagen del billete, diga si es auténtico o falso.

## 2. Objetivo

| Nivel | Descripción |
|---|---|
| **Negocio** | Reducir a casi cero los billetes falsos que se aceptan, sin rechazar billetes buenos de forma excesiva |
| **Ciencia de datos** | Clasificar un billete como auténtico o falso a partir de 4 características de su imagen |
| **Tipo de problema** | Clasificación binaria |
| **Variable objetivo** | `class` (0 = auténtico, 1 = falso) |

## 3. Criterios de éxito

| Tipo | Métrica | Umbral |
|---|---|---|
| Negocio (KPI) | Tasa de rechazo de billetes buenos | ≤ 2 % |
| Modelo | Recall de la clase falso | ≥ 0,99 |
| *Baseline* a superar | Predecir siempre "auténtico" (clase mayoritaria) | Exactitud 55,5 % |

## 4. Datos

| Fuente | Descripción | Filas × columnas | Acceso |
|---|---|---|---|
| https://archive.ics.uci.edu/dataset/267/banknote+authentication | Características wavelet de imágenes de billetes | 1372 × 5 | Público, descargado el 2026-11-21 |

**¿Qué representa una fila?** Un billete, con 4 características numéricas de su imagen y su clase.

## 5. Alcance

- **Incluye:** limpieza, EDA, *baseline*, comparación de modelos, pipeline de entrenamiento reproducible y una API con `/health` y `/predict`.
- **No incluye:** el procesamiento de imágenes (las características ya vienen calculadas), integración con hardware de cajeros ni despliegue en producción real.

## 6. Riesgos y supuestos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Resultados casi perfectos que parecen sospechosos | Alta | Medio | Validación cruzada, conjunto de prueba usado una sola vez y explicar que las clases están muy separadas |
| Dataset pequeño (1372 filas) | Alta | Medio | Validación cruzada estratificada y modelos simples |
| Posibles duplicados en los datos | Media | Medio | Revisarlos en la limpieza y evitar que caigan en entrenamiento y prueba a la vez |
| Fuga de información (*data leakage*) | Baja | Alto | Ajustar el escalado solo con los datos de entrenamiento, dentro del pipeline |
| Un solo integrante para todo el trabajo | Alta | Alto | Priorizar lo mínimo exigido y documentar mientras se avanza |

## 7. Plan

| Día | Fase CRISP-DM | Entregable | Responsable |
|---|---|---|---|
| Sáb 21 nov | Negocio + Datos | Charter + KPIs + perfil inicial | Lina Marcela Carvajal Perez |
| Dom 22 nov | Preparación + EDA | Limpieza + `notebooks/05_eda.ipynb` | Lina Marcela Carvajal Perez |
| Lun 23 nov | Modelado + Despliegue | *Baseline*, pipeline y API | Lina Marcela Carvajal Perez |
| Mar 24 nov | Evaluación | Presentación, ensayo y revisión de entrega | Lina Marcela Carvajal Perez |
| Mié 25 nov | Sustentación | Presentación final | Lina Marcela Carvajal Perez |

## 8. Stakeholders

| Persona/rol | Interés | Cómo se le comunica |
|---|---|---|
| Responsable de operaciones de cajeros o cajas | No aceptar billetes falsos y no molestar a los clientes | Presentación final con la demo de la API |
| Profesora del curso | Proyecto completo, reproducible y bien comunicado | Repositorio y sustentación |
