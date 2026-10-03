# Paso 5 – POI y capas complementarias

**Notebook:** `02_poi_y_capas`

## Objetivo
Incorporar el equipamiento urbano y el contexto territorial, e integrarlos espacialmente al grafo.

## Capas de equipamiento (mínimo exigido: al menos una capa)
| Capa | Etiquetas OSM sugeridas |
|---|---|
| Hospitales y centros de salud | `amenity=hospital`, `amenity=clinic`, `healthcare=*` |
| Colegios | `amenity=school` |
| Mercados | `amenity=marketplace`, `shop=supermarket` (decidir si se incluye) |

Descarga con `ox.features_from_polygon(poligono, tags)`.

## Capas de contexto (opcionales, recomendadas)
- Límites de distrito (ya del paso 2).
- Parques (`leisure=park`), manzanas/uso de suelo (`landuse=*`) si están disponibles.
- Barreras físicas: vías rápidas, ríos/quebradas, vías férreas (para la discusión de resultados).

## Tareas
1. Descargar cada capa y guardarla en `data/raw/` con fecha.
2. Reducir geometrías de polígono a puntos representativos (centroide) cuando el POI venga como polígono; ojo con hospitales grandes con varias entradas.
3. Proyectar a EPSG:32718.
4. Conteo de POI por tipo y por distrito, y revisión de duplicados.
5. **Integración al grafo:** asignar cada POI al nodo peatonal más cercano (`ox.nearest_nodes`) y registrar la **distancia de snap**. Si un POI queda a más de un umbral (p. ej. 100 m), marcarlo y decidir si se descarta.
6. **Validación cruzada (si hay tiempo):** comparar el conteo de colegios y establecimientos de salud en OSM con ESCALE/SUSALUD para estimar la completitud de OSM.

## Entregable
- GeoPackage de POI con columna `nodo_osmid` y `dist_snap_m`.
- Tabla de conteo por tipo y distrito.

## Riesgos
- OSM puede tener pocos hospitales; puede ser necesario incluir centros de salud para tener un análisis útil. Decidir el criterio y justificarlo.
