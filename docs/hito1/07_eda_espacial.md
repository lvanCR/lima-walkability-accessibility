# Paso 7 – Análisis exploratorio espacial

**Notebook:** `03_metricas_y_eda`

## Objetivo
Entender la estructura y calidad del territorio modelado antes de calcular métricas más complejas.

## Tareas
1. **Vista general:** mapa de la red (aristas) con límites distritales y POI.
2. **Atributos de aristas:**
   - distribución de `length` (histograma, boxplot por distrito),
   - frecuencia de tipos de `highway` (footway, residential, steps, path, etc.) por distrito,
   - presencia de escaleras (`steps`) como indicador de topografía/obstáculo.
3. **Densidad:**
   - nodos y aristas por km²,
   - longitud total de vía por km²,
   - densidad de intersecciones (nodos con `street_count` ≥ 3) por km².
4. **Estructura de manzanas:** distribución de `street_count` (grados de intersección) y orientación de calles (diagrama polar de rumbos con `ox.bearing`; entropía de orientación) por distrito.
5. **Distribución de POI:** conteo y mapa de calor/ubicaciones; distancia de snap.
6. **Comparación Miraflores vs SJM:** todo lo anterior normalizado por área o por número de nodos (obligatorio por el enunciado).
7. **Control de calidad:** zonas con aparente baja densidad de datos (posibles vacíos de OSM).

## Hallazgos a anotar
Qué diferencias aparecen entre distritos, qué parece anómalo y qué hipótesis plantea para la accesibilidad.

## Entregable
Figuras en `figures/plots/` y `figures/maps/` y un resumen de 5–8 hallazgos.
