# lima-walkability-accessibility

**Accesibilidad peatonal a equipamiento urbano en Lima (Miraflores y San Juan de Miraflores) mediante áreas de servicio (isócronas).**

Proyecto parcial-final del curso *Complex Networks* (Ciencias de la Computación, 2026-2). Tema 4: accesibilidad a equipamiento urbano (salud, educación y mercados) sobre el grafo peatonal de OpenStreetMap.

## Estado

| Hito | Contenido | Estado |
|---|---|---|
| Hito 1 (parcial) | Datos, limpieza, exploración espacial, métricas, mapas y pipeline | Análisis y figuras completos. Pendiente por el equipo: informe, exposición y video |
| Hito 2 (final) | Isócronas de 5, 10 y 15 min, cobertura, comparación entre distritos y artículo | Por hacer (`notebooks/04`, `05` y `docs/hito2`) |

## Estructura

```
notebooks/   análisis, en orden de ejecución
  01_descarga_y_limpieza      descarga del grafo (Colab), carga, inventario, limpieza y efecto de simplify
  01b_efecto_simplify_colab   descarga sin simplificar para medir el efecto de simplify (Colab)
  02a_poi_descarga_colab      descarga de POI y capas de contexto (Colab)
  02b_poi_integracion         deduplicación de POI y asignación al nodo más cercano
  02c_construccion_red        definición del grafo, ponderación por tiempo e isócrona de prueba
  03_metricas_y_eda           análisis exploratorio espacial y métricas globales y locales
  03b_mapas_hito1             figuras finales del Hito 1
  04, 05                      esqueletos del Hito 2
src/         config.py (parámetros), red.py (grafo ponderado), mapas.py (escala, norte, guardado)
data/        raw/ (descargas), interim/ (grafo limpio), processed/ (tablas)
figures/     maps/, plots/ y CATALOGO.md (pie de cada figura)
docs/        hito1/ (plan por pasos y pipeline), hito2/ (notas)
reports/     informe del Hito 1 y artículo del Hito 2 (a cargo del equipo)
video/       videos de exposición (no se versionan)
```

## Cómo reproducir

1. Crear el entorno: `python -m venv .venv`, activarlo y `pip install -r requirements.txt` (Python 3.12).
2. **Con acceso a Overpass (se hizo en Google Colab):** celdas de descarga de `01`, y notebooks `01b` y `02a`. Dejan los archivos en `data/raw/`.
3. **Sin red, en local y en este orden:** carga y limpieza de `01` → `02b` → `02c` → `03` → `03b`.
4. Los parámetros (semilla 42, buffers, velocidad de caminata, umbrales) están en `src/config.py`.

Descripción completa del flujo en [`docs/hito1/10_pipeline_metodologico.md`](docs/hito1/10_pipeline_metodologico.md).

## Datos y reproducibilidad

- Los datos de `data/raw`, `data/interim` y los GeoPackage **no se versionan** (pesan decenas de MB y OSM cambia con el tiempo). Se versionan los registros de cada descarga, con fecha, consulta, versiones de librerías y SHA-256 de los archivos:
  - `data/raw/descarga_log.json` (grafo, descargado el 2026-10-03 21:50 UTC)
  - `data/raw/poi_descarga_log.json` (POI, 22:02 UTC)
  - `data/raw/simplify_comparacion.json` (comparación de `simplify`, 23:21 UTC)
- Los archivos descargados se pueden compartir por separado para verificar los hashes.
- Las tablas pequeñas de resultados están en `data/processed/*.csv`.

## Resultados del Hito 1 (resumen)

- Grafo peatonal limpio: 17 265 nodos y 51 216 aristas en EPSG:32718, con un componente por distrito (Miraflores y San Juan de Miraflores no son contiguos).
- 583 POI válidos integrados al grafo: 74 de salud, 407 de educación y 102 de mercados.
- Redes espaciales sin hubs y sin efecto de mundo pequeño; densidad de red casi igual en ambos distritos (≈ 407 y 414 nodos/km²) pero con composición distinta (SJM: más escaleras y vías locales).
- `simplify=True` reduce los nodos un 58 % conservando intersecciones y longitud total.
- Limitación principal: efecto de borde (`docs/hito2/01_nota_ampliar_grafo.md`).

## Atribución

Datos © OpenStreetMap contributors, disponibles bajo la licencia ODbL (<https://www.openstreetmap.org/copyright>).
