# Paso 8 – Primeras métricas globales y locales

**Notebook:** `03_metricas_y_eda`

## Métricas globales (por distrito y para el grafo completo)
| Métrica | Herramienta | Nota |
|---|---|---|
| Nº de nodos y aristas | networkx | |
| Grado medio | networkx | |
| Densidad de intersecciones / km² | `ox.basic_stats(area=...)` | Área en m² del polígono proyectado |
| Longitud total de vía y por km² | osmnx | |
| Circuity (sinuosidad) | `ox.basic_stats` | Cociente longitud de ruta / distancia en línea recta |
| Número de componentes | networkx | |
| Diámetro y longitud media de camino | networkx | Costoso; para grafos grandes, estimar con muestreo y declarar el tamaño |
| Eficiencia global | networkx / muestreo | Idem; declarar si es aproximada |

## Métricas locales
| Métrica | Observación |
|---|---|
| Distribución de grado | Histograma; esperar grados bajos (red espacial planar, sin hubs) |
| Coeficiente de agrupamiento | En versión no dirigida y sin multiaristas |
| Centralidad de grado | |
| Centralidad de cercanía (closeness) | Ponderada por longitud |
| Centralidad de intermediación (betweenness) | **Aproximada con `k` muestras** si el grafo es grande: declarar `k`, fijar semilla y discutir el error |
| PageRank | |

## Interpretación espacial
- Mapear al menos betweenness y closeness sobre el grafo.
- Preguntas guía: ¿qué calles concentran flujo potencial?, ¿dónde queda el "centro" funcional?, ¿difiere entre distritos?

## Validaciones
- Probar la sensibilidad de betweenness al tamaño de muestra `k` (p. ej. k = 100, 300, 1 000) comparando correlación de rankings.
- Verificar que las métricas dependientes de escala estén normalizadas por área o número de nodos.

## Entregable
- `data/processed/metricas_globales.csv` y `metricas_nodos.gpkg`.
- Tabla comparativa Miraflores vs SJM para las diapositivas.
