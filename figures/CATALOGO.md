# Catálogo de figuras – Hito 1

Todas las figuras se guardan a 200 dpi. Los mapas llevan escala, flecha de norte, leyenda y fuente (© OpenStreetMap contributors); el CRS es EPSG:32718. Los notebooks que las generan son `03_metricas_y_eda` (prefijos `eda_` y `metricas_`) y `03b_mapas_hito1` (prefijo `hito1_`).

Correspondencia con la lista mínima del plan (`docs/hito1/09_mapas_y_visualizaciones.md`):

| # del plan | Figura | Archivo |
|---|---|---|
| 1 | Área de estudio | `maps/hito1_01_area_estudio.png` |
| 2 y 3 | Red por tipo de vía y POI sobre la red (en una sola figura) | `maps/eda_01_red_por_tipo_via.png` |
| 4 | Intermediación (y cercanía) | `maps/metricas_02_intermediacion.png`, `maps/metricas_03_cercania.png` |
| 5 | Longitud de aristas | `plots/eda_03_longitudes.png` |
| 6 | Distribución de grado | `plots/metricas_01_distribucion_grado.png` |
| 7 | Orientación de calles | `plots/eda_05_orientacion.png` |
| 8 | Datos faltantes | `plots/hito1_08_datos_faltantes.png` |
| 9 | Isócrona de prueba | `maps/hito1_09_isocrona_prueba.png` |
| extra | Densidad de nodos; composición por tipo de vía | `maps/eda_02_densidad_nodos.png`, `plots/eda_04_composicion_vias.png` |

---

## Mapas

### `maps/hito1_01_area_estudio.png`
**Pregunta:** ¿Qué territorio se analiza y dónde termina cada zona de datos?
**Pie:** Área de estudio: Miraflores (9.45 km²) y San Juan de Miraflores (22.06 km²), distritos no contiguos de Lima Metropolitana. La línea roja discontinua marca el límite del grafo peatonal (distritos + 300 m) y la punteada la zona de descarga de POI (distritos + 1 200 m). En verde, parques; en rojo, vías rápidas (`trunk`/`motorway`), que funcionan como barrera física. No se encontraron ferrocarriles ni ríos en OSM dentro de la zona.

### `maps/eda_01_red_por_tipo_via.png`
**Pregunta:** ¿Cómo es la red y dónde está el equipamiento?
**Pie:** Red peatonal por tipo de vía (arterial, local, peatonal y escaleras) y 583 POI de equipamiento integrados al grafo: salud (cruz roja), educación (cuadrado verde) y mercados (rombo amarillo). Las escaleras (violeta) se concentran en las laderas del noreste y del centro-oeste de San Juan de Miraflores.

### `maps/eda_02_densidad_nodos.png`
**Pregunta:** ¿Dónde es más densa la red y dónde no hay red?
**Pie:** Densidad de nodos de la red peatonal en celdas de 250 m. Máximo de unos 1 800 nodos/km² en el oeste de San Juan de Miraflores; el centro-sur de ese distrito es el de menor densidad. Los valores medios son casi iguales en ambos distritos (407 y 414 nodos/km²).

### `maps/metricas_02_intermediacion.png`
**Pregunta:** ¿Qué calles concentran los caminos más cortos?
**Pie:** Centralidad de intermediación aproximada (k = 500 orígenes, ponderada por longitud), en escala logarítmica y con la misma escala de color en ambos distritos. Los valores altos siguen unos pocos ejes arteriales. El ranking aproximado reproduce el exacto en Miraflores con una correlación de Spearman de 0.989.

### `maps/metricas_03_cercania.png`
**Pregunta:** ¿Qué zonas están más cerca, en promedio, de todo el distrito?
**Pie:** Centralidad de cercanía (inversa de la distancia media por la red a los demás nodos del distrito). En Miraflores es máxima en el centro y cae hacia los extremos; en San Juan de Miraflores crece hacia el eje central. Los valores no son comparables entre distritos (dependen del tamaño de la red); se comparan los patrones.

### `maps/hito1_09_isocrona_prueba.png`
**Pregunta:** ¿Qué alcanza una persona caminando desde un hospital y cómo afecta el límite del grafo?
**Pie:** Isócrona de prueba desde el Hospital Central FAP, a 4.8 km/h: 105 nodos a 5 min, 272 a 10 min y 634 a 15 min. El hospital está en el borde norte de Miraflores, y la isócrona llega hasta el límite del grafo (línea roja discontinua): el cálculo se trunca allí y subestima lo alcanzable (efecto de borde). Es una prueba del método; el cálculo completo corresponde al Hito 2.

---

## Gráficos

### `plots/eda_03_longitudes.png`
**Pregunta:** ¿Qué longitud tienen los tramos de calle?
**Pie:** Distribución de la longitud de arista en cada distrito (histograma recortado a 200 m y boxplot sin atípicos). Las medias son casi iguales (47.1 m en Miraflores y 46.4 m en San Juan de Miraflores).

### `plots/eda_04_composicion_vias.png`
**Pregunta:** ¿De qué tipo de vía está hecha la red?
**Pie:** Composición de la longitud de vía por tipo. Miraflores tiene más vía arterial (25.8 %) y peatonal (27.1 %); San Juan de Miraflores es más local (61.2 %) y tiene un 4.9 % de escaleras frente a 0.2 % en Miraflores.

### `plots/metricas_01_distribucion_grado.png`
**Pregunta:** ¿Hay nodos hub?
**Pie:** Distribución de grado del grafo no dirigido. La mayoría de los nodos tiene grado 3 (55 % y 68 %) o 4 (25 % y 20 %), y el grado máximo es 7 y 6: no hay hubs, como corresponde a una red espacial planar.

### `plots/eda_05_orientacion.png`
**Pregunta:** ¿Tiene la red una cuadrícula?
**Pie:** Orientación de las calles ponderada por longitud (36 clases de 10°). Miraflores muestra cuatro picos en N–S y E–O (entropía H = 3.41, índice de orden φ = 0.15); San Juan de Miraflores no tiene dirección dominante (H = 3.52, φ = 0.06), coherente con un trazado adaptado a laderas.

### `plots/hito1_08_datos_faltantes.png`
**Pregunta:** ¿Qué tan completos son los atributos de OSM?
**Pie:** Porcentaje de aristas sin dato en `name`, `maxspeed` y `lanes` en el grafo limpio. Faltan más datos en San Juan de Miraflores (57 %, 88 % y 78 %) que en Miraflores (43 %, 50 % y 51 %). Los atributos no se imputan: el análisis peatonal usa velocidad de caminata constante y no los necesita.

### `plots/hito1_10_efecto_simplify.png`
**Pregunta:** ¿Cómo cambia el conteo de nodos al simplificar el grafo?
**Pie:** Efecto de `simplify=True` sobre los nodos de cada distrito (izquierda) y sobre la densidad de nodos por km² (derecha). La simplificación elimina el 63.8 % de los nodos de Miraflores y el 52.3 % de los de San Juan de Miraflores. Sin simplificar, Miraflores parece 29 % más denso que San Juan de Miraflores (1 150 frente a 889 nodos/km²); simplificado, las densidades son casi iguales (416 frente a 425). Datos del grafo antes de la limpieza.

### `plots/hito1_11_pipeline.png`
**Pregunta:** ¿Cómo se llega de los datos de OpenStreetMap a los resultados?
**Pie:** Pipeline metodológico del Hito 1 en ocho etapas: datos de OSM, respaldo reproducible, limpieza y proyección, integración de POI, construcción de la red, análisis exploratorio, métricas y, pendiente para el Hito 2, isócronas y cobertura. Cada etapa indica el notebook que la ejecuta. Descripción en `docs/hito1/10_pipeline_metodologico.md`.
