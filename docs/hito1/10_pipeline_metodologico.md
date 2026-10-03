# Paso 10 – Pipeline metodológico

## Objetivo
Un diagrama y una descripción que expliquen el flujo completo, desde el dato hasta el resultado, para la presentación del Hito 1 y para la sección 3 del artículo.

## Flujo propuesto
```
Límites (OSM) ──► Descarga grafo walk ──► Grafo crudo (GraphML + log + hash)
                                              │
                                              ▼
                              Carga + inventario + datos faltantes
                                              │
                                              ▼
                       Limpieza: componente gigante, atributos, proyección EPSG:32718
                                              │
              POI (OSM) ──► proyección ──► snap al nodo más cercano
                                              │
                                              ▼
                       Grafo ponderado (longitud, tiempo a 4.8 km/h)
                                              │
                          ┌───────────────────┴───────────────────┐
                          ▼                                       ▼
                 EDA espacial y densidades              Métricas globales y locales
                          └───────────────────┬───────────────────┘
                                              ▼
                                  Mapas y hallazgos preliminares
                                              │
                                              ▼
                          (Hito 2) Isócronas 5/10/15 min, cobertura, comparación
```

## Elementos a documentar
- Entradas y salidas de cada etapa (ver tablas en los pasos 2–9).
- Parámetros clave: `network_type`, buffer, umbral de snap, velocidad, `k` de betweenness, semilla.
- Herramientas por etapa (osmnx, networkx, geopandas, shapely, rtree, matplotlib).
- Puntos de control de calidad (conteos antes/después, hash, nodos mínimos).

## Entregable
Diagrama limpio (puede hacerse en PowerPoint, draw.io o Mermaid) y una descripción de media página.
