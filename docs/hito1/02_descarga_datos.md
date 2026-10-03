# Paso 2 – Descarga de datos

**Notebook:** `01_descarga_y_limpieza`

## Objetivo
Obtener el grafo peatonal desde OpenStreetMap y dejar un respaldo que haga el trabajo reproducible.

## Tareas
1. Fijar semilla (`SEED=42`) y registrar versiones: Python, osmnx, networkx, geopandas, shapely, numpy, pandas.
2. Obtener los polígonos de límite de Miraflores y SJM con `ox.geocode_to_gdf`.
3. Unir ambos polígonos (opcionalmente con un pequeño buffer, p. ej. 200–500 m, para reducir efecto de borde; decidir y justificar).
4. Descargar el grafo: `ox.graph_from_polygon(poligono, network_type='walk', simplify=True)`.
5. Guardar el grafo **crudo** en `data/raw/` (GraphML).
6. Registrar en un archivo `data/raw/descarga_log.json`:
   - fecha y hora de descarga,
   - consulta exacta (lugares, `network_type`, buffer, parámetros),
   - versiones de librerías,
   - número de nodos y aristas descargados,
   - hash (SHA-256) del GraphML.

## Consideraciones
- La API Overpass puede dar timeout (ya ocurrió en la prueba con Cusco). Dejar `ox.settings.timeout` alto y reintentar; mantener la caché de osmnx.
- OSM cambia con el tiempo: nunca volver a descargar para "actualizar" sin registrar una nueva fecha.
- `data/raw/` está excluido de Git: el hash y el log permiten verificar el archivo. Si el docente necesita los datos, compartirlos por separado o quitar la exclusión.

## Entregable
- `data/raw/*.graphml` y `data/raw/descarga_log.json`.

## Criterio de aceptación
El notebook, ejecutado desde cero, produce el mismo archivo (o uno con fecha distinta claramente registrada).
