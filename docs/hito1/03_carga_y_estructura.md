# Paso 3 – Carga e inventario del grafo

**Notebook:** `01_descarga_y_limpieza`

## Objetivo
Cargar el grafo desde disco (no desde la API) y entender qué contiene antes de limpiarlo.

## Tareas
1. Cargar con `ox.load_graphml`.
2. Verificar tipo (`MultiDiGraph`), CRS (esperado EPSG:4326 antes de proyectar) y atributos de nodos (`x`, `y`, `street_count`, etc.).
3. Convertir a GeoDataFrames con `ox.graph_to_gdfs` (nodos y aristas).
4. Inventario:
   - número de nodos y aristas,
   - columnas disponibles en aristas (`highway`, `length`, `name`, `oneway`, `maxspeed`, `lanes`, `bridge`, `tunnel`, `geometry`…),
   - tipos de datos y valores únicos de `highway` (puede ser lista en aristas simplificadas),
   - aristas paralelas y bucles (self-loops).
5. Tabla de **datos faltantes** por atributo (% de aristas sin `name`, `maxspeed`, `lanes`, etc.). El enunciado lo exige.

## Entregable
- Tabla de inventario y tabla de datos faltantes (para el informe y las diapositivas).

## Nota
Los atributos con listas (`highway`, `name`, etc.) aparecen cuando la simplificación fusiona segmentos; hay que normalizarlos en el paso de limpieza.
