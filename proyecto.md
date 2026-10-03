# Enunciado Proyecto Parcial – Final

**Curso:** Complex Networks
**Escuela:** Ciencias de la Computación – Pregrado
**Periodo:** 2026-2
**Modalidad:** Trabajo en equipo, 3 integrantes por grupo.

---

## Logro del curso

Al finalizar el curso, el estudiante presenta un proyecto de aplicación de ciencia de datos espaciales evidenciando el uso de técnicas y herramientas de teoría de grafos y redes complejas sobre datos geográficos abiertos, así como su correcta explicabilidad, para generar acciones y resultados específicos que le permitan explotar, interpretar y comunicar perspectivas de la estructura del territorio.

---

## Contexto

Una red vial urbana obtenida de OpenStreetMap (OSM) puede representarse como un grafo dirigido y ponderado G = (V, E), donde los nodos son intersecciones (y finales de vía) y las aristas son segmentos de calle. A diferencia de una red abstracta, este es un grafo espacial: cada nodo tiene coordenadas (latitud, longitud) y cada arista tiene atributos geométricos y semánticos: longitud en metros, tipo de vía (highway), número de carriles, sentido (oneway), velocidad máxima y tiempo de viaje estimado.

Adicionalmente, OSM permite descargar capas de puntos de interés (POI): hospitales, colegios, mercados, farmacias, comisarías, paraderos y estaciones de transporte, además de polígonos de manzanas, parques y límites administrativos. Estas capas se integran al grafo mediante operaciones espaciales (unión al nodo más cercano, buffers, joins espaciales) y funcionan como metadatos que enriquecen la interpretación de los resultados.

Los equipos deberán seleccionar un área de estudio y uno de los temas propuestos, y desarrollar un proyecto de investigación aplicado, dividido en dos hitos.

---

## Datos y área de estudio

A diferencia de otros trabajos del curso, aquí **no** se entrega un dataset cerrado: cada equipo construye su propio conjunto de datos descargándolo de OpenStreetMap mediante osmnx (API Overpass). Reglas mínimas:

- **Área de estudio:** uno o más distritos de Lima Metropolitana o de una ciudad del Perú (Arequipa, Trujillo, Cusco, Piura, Iquitos, entre otras). Cada equipo debe elegir un área distinta; se asigna por orden de inscripción en el aula virtual.
- **Tamaño mínimo:** el grafo debe tener al menos 3 000 nodos y 6 000 aristas. Tamaño máximo recomendado: 60 000 nodos, para que los cálculos de centralidad sean factibles en clase.
- **Tipo de red:** se debe justificar el `network_type` elegido (`'drive'`, `'walk'`, `'bike'` o `'all'`). Los temas de accesibilidad peatonal exigen `'walk'`; los de tránsito exigen `'drive'`.
- **Capas complementarias:** al menos una capa de POI o de polígonos (equipamiento urbano, límites de manzana, parques o zonificación) integrada espacialmente al grafo.
- **Reproducibilidad:** el notebook debe guardar el grafo descargado en disco (GraphML o GeoPackage) y registrar la fecha de descarga, la consulta usada y la versión de las librerías. OSM cambia con el tiempo; sin ese respaldo el trabajo no es reproducible.
- **Proyección:** todo cálculo de distancias, áreas o densidades debe hacerse sobre el grafo proyectado a un CRS métrico (UTM 18S / EPSG:32718 para Lima), nunca en grados.

---

## Fases y entregables

### Hito 1 – Parcial

- **Contenido:** definición y justificación del área de estudio, descarga y limpieza del grafo, análisis exploratorio espacial, primeras métricas globales y locales, mapas y visualizaciones preliminares, pipeline metodológico.
- **Exposición en clase:** 10 minutos por grupo.
- **Video:** presentación de 10 minutos con hallazgos preliminares.
- **Evaluación:** corresponde al Trabajo Parcial (EA1).

### Hito 2 – Final

- **Contenido:** desarrollo completo del proyecto en formato de artículo científico, con resultados, discusión y conclusiones.
- **Exposición en clase:** 10 minutos por grupo.
- **Video:** presentación de 10 minutos con resultados y conclusiones.
- **Evaluación:** corresponde al Proyecto Final (EB1).

---

## Tema del proyecto

### 4. Accesibilidad a equipamiento urbano mediante áreas de servicio

**Explicación:** Calcular isócronas (áreas alcanzables en 5, 10 y 15 minutos caminando) desde hospitales, colegios o mercados usando el grafo peatonal.

**Resultados potenciales:** Mapas de cobertura, porcentaje de nodos y de superficie cubierta, detección de zonas desatendidas y comparación de la accesibilidad entre áreas de distinto nivel socioeconómico o densidad.

---

## Herramientas y entorno de trabajo

El proyecto se desarrolla en Python 3 sobre Jupyter Notebook o VS Code. Los paquetes sugeridos son:

| Paquete | Uso previsto en el proyecto |
|---|---|
| `osmnx` | Descarga, construcción, simplificación y proyección del grafo desde OpenStreetMap; métricas espaciales (circuity, densidad de intersecciones), isócronas y orientación de calles. |
| `networkx` | Representación del grafo, métricas globales y locales, centralidades, componentes, caminos más cortos, comunidades y simulaciones de robustez. |
| `geopandas` | Manejo de nodos, aristas y POI como GeoDataFrames; joins espaciales, buffers, cambio de sistema de coordenadas y exportación a GeoPackage o Shapefile. |
| `numpy` | Cálculo vectorizado, muestreo aleatorio de pares origen–destino y estadística de las distribuciones obtenidas. |
| `matplotlib` | Mapas estáticos, histogramas de grado, diagramas polares de orientación de calles y curvas de degradación. |
| `python3-rtree` | Índice espacial que acelera los joins y las consultas de vecino más cercano en geopandas; requisito de sistema, no solo de pip. |
| `shapely` | Operaciones geométricas sobre segmentos y polígonos (intersección, distancia, envolventes). |
| Complementarios (opcionales) | folium o keplergl para mapas interactivos; python-louvain o igraph para comunidades; scipy para árboles KD y estadística; contextily para mapas base. |

> **Requisitos de reproducibilidad:** entorno documentado (`requirements.txt` o `environment.yml`), semilla aleatoria fijada, notebooks versionados en un repositorio Git público o privado compartido con el docente, y datos intermedios exportados. Se penaliza el código que solo funciona en la máquina de un integrante.

---

## Restricciones y consideraciones metodológicas

- OpenStreetMap es una fuente colaborativa: la completitud de los atributos varía por zona. El equipo debe reportar el porcentaje de aristas con datos faltantes en `maxspeed`, `lanes` o `name`, y explicar cómo trató esos vacíos.
- Las centralidades exactas son costosas. Para grafos grandes se admite betweenness aproximada por muestreo (parámetro `k`), siempre que se declare el tamaño de muestra y se discuta el error.
- Toda métrica que dependa de la escala (densidad, longitud total, número de intersecciones) debe normalizarse por área o por número de nodos para que la comparación entre distritos sea válida.
- El grafo de OSM incluye nodos de geometría; usar `simplify=True` y explicar el efecto de la simplificación sobre el conteo de nodos.
- Los resultados deben interpretarse con prudencia: la red vial es una aproximación del territorio, no un modelo de tránsito real. No se admiten conclusiones sobre flujo vehicular observado sin datos de aforo.

---

## Criterios de evaluación

| Criterio | Peso | Descripción |
|---|:---:|---|
| Construcción y calidad del dato | 15 % | Pertinencia del área elegida, corrección de la descarga, proyección, limpieza e integración de capas complementarias. |
| Rigor en el análisis de red | 30 % | Uso correcto de métricas y algoritmos, justificación de los parámetros, validación de los resultados y control de sesgos de escala. |
| Visualización y cartografía | 15 % | Claridad de mapas y gráficos, escala, leyenda, norte, paleta adecuada y coherencia entre figura y texto. |
| Interpretación y explicabilidad | 20 % | Conexión de los hallazgos con la teoría del curso y con el contexto urbano; discusión de limitaciones. |
| Reproducibilidad y código | 10 % | Notebook ejecutable de principio a fin, entorno documentado, código legible y versionado. |
| Comunicación (exposición y video) | 10 % | Dominio del tema, uso del tiempo, calidad del material y respuesta a preguntas. |

---

## Anexo: Plantilla del artículo científico

### Título del artículo

*(Claro y breve; debe reflejar el fenómeno espacial analizado y el área de estudio.)*

### Autores

*(Integrantes del equipo, institución, curso y periodo académico.)*

### Resumen (Abstract)

- Problema abordado y objetivo del estudio.
- Área de estudio y origen de los datos.
- Metodología principal (construcción del grafo, métricas de red, algoritmos).
- Principales resultados obtenidos.
- Conclusiones clave.

*Extensión sugerida: 200–250 palabras.*

### Palabras clave

*(3 a 5 términos: p. ej., redes complejas, grafos espaciales, OpenStreetMap, accesibilidad, centralidad.)*

### 1. Introducción

- Contexto del problema urbano y motivación.
- Relevancia del caso de estudio elegido.
- Conexión con las teorías vistas en clase (small-world, scale-free, grafos planares y espaciales, percolación, comunidades, resiliencia).
- Objetivo general y objetivos específicos.

### 2. Marco Teórico

- Conceptos centrales de teoría de grafos y redes complejas aplicables al proyecto.
- Particularidades de las redes espaciales frente a las redes abstractas: restricción planar, costo de las aristas, ausencia de hubs de grado alto.
- Métricas y modelos relevantes según el tema (centralidades, modularidad, eficiencia global, circuity, entropía de orientación, SIR/umbral, p-mediana).
- Breve revisión de trabajos previos o aplicaciones similares.

### 3. Metodología

#### 3.1 Datos

- Área de estudio: delimitación, extensión y criterio de selección.
- Consulta a OpenStreetMap: función utilizada, `network_type`, fecha de descarga y versión de osmnx.
- Descripción del grafo obtenido: número de nodos y aristas, atributos disponibles y porcentaje de valores faltantes.
- Capas complementarias (POI, manzanas, límites) y su procedencia.
- Limpieza y normalización: simplificación, tratamiento de componentes desconectados, imputación o descarte de atributos faltantes, proyección al CRS métrico.

#### 3.2 Construcción de la red

- Definición formal del grafo: qué representa un nodo, qué representa una arista.
- Dirigido o no dirigido; justificación respecto del atributo `oneway`.
- Criterio de ponderación de aristas (longitud, tiempo de viaje, penalización por tipo de vía) y su justificación.
- Integración espacial de las capas complementarias (vecino más cercano, buffer, join espacial).

#### 3.3 Análisis y métricas

- **Métricas globales:** número de nodos y aristas, grado medio, densidad de intersecciones por km², longitud total de vía, circuity, eficiencia global, diámetro y número de componentes.
- **Métricas locales:** distribución de grado, coeficiente de agrupamiento, centralidades (grado, cercanía, intermediación, PageRank) y su interpretación espacial.
- **Procedimientos específicos:** cálculo de isócronas a 5, 10 y 15 minutos, porcentaje de cobertura de nodos y superficie, detección de zonas desatendidas.
- **Validaciones y comparaciones:** contrastes entre áreas de distinto nivel socioeconómico o densidad poblacional.

#### 3.4 Herramientas

- Software y librerías: Python (osmnx, networkx, geopandas, numpy, matplotlib, python3-rtree), y opcionalmente QGIS, Gephi o kepler.gl.
- Reproducibilidad: scripts y notebooks versionados, semillas aleatorias, archivo de entorno y grafo exportado.

### 4. Resultados

- Presentación de métricas, tablas y visualizaciones.
- Cartografía: al menos tres mapas con escala, orientación y leyenda.
- Mapas de isócronas y cobertura del equipamiento urbano.
- Tablas comparando accesibilidad entre zonas o tipos de equipamiento.

### 5. Discusión

- Interpretación de los hallazgos frente a los objetivos.
- Relación con los atributos del territorio: tipo de vía, equipamiento, barreras físicas, morfología urbana.
- Coherencia con las teorías de redes (mundo pequeño, planaridad, resiliencia, comunidades).
- Limitaciones: completitud de OSM, supuestos del modelo, efectos de borde del área de estudio, sensibilidad a los parámetros.

### 6. Conclusiones

- Principales hallazgos y su relevancia.
- Implicancias prácticas para la planificación urbana o la gestión del territorio.
- Recomendaciones para trabajos futuros.

### 7. Referencias

- Usar formato APA.
- Citar la bibliografía base del curso, artículos adicionales y, obligatoriamente, la atribución a OpenStreetMap y a sus contribuyentes.

### 8. Anexos

- Código fuente, figuras complementarias y tablas extendidas.
- Consulta exacta de descarga, fecha y hash del grafo utilizado.
- Detalles técnicos y configuraciones reproducibles.
