# Resumen de resultados del Hito 1 (material para el informe)

Todas las cifras salen de los notebooks y archivos indicados. Los valores que dependen de la fecha de descarga de OSM corresponden a la descarga del **2026-10-03**. Distritos: Miraflores (9.45 km²) y San Juan de Miraflores, SJM (22.06 km²).

## 1. Datos (sección 3.1 del artículo)

| Elemento | Valor | Fuente |
|---|---|---|
| Descarga del grafo | 2026-10-03 21:50 UTC, `ox.graph_from_polygon`, `walk`, `simplify=True`, `retain_all=True`, buffer 300 m | `data/raw/descarga_log.json` |
| Grafo crudo | 17 834 nodos, 52 768 aristas, 112 componentes | idem |
| Nodos por zona (crudo) | SJM 9 367 · Miraflores 3 928 · fuera de los distritos (buffer) 4 539 | idem |
| POI y contexto | 2026-10-03 22:02 UTC, buffer 1 200 m: salud 126, educación 748, mercados 205, parques 971, barreras 180 (todas vías rápidas; sin ferrocarriles ni ríos en OSM) | `data/raw/poi_descarga_log.json` |
| Entorno de descarga | Colab: Python 3.13.15, osmnx 2.1.1, networkx 3.6.1, geopandas 1.1.4 | logs |
| Entorno de análisis | Local: Python 3.12.2, osmnx 2.1.1, networkx 3.6.1, geopandas 1.2.0 | `requirements.txt` |

**Efecto de `simplify=True`** (`01`, sección final; `data/raw/simplify_comparacion.json`): sin simplificar 42 545 nodos y 102 158 aristas; simplificado 17 787 y 52 642 (−58.2 % y −48.5 %). Los nodos de geometría (`street_count = 2`) pasan de 24 711 a 202 (−99.2 %); las intersecciones pasan de 15 729 a 15 480 y las calles sin salida se mantienen (2 105). Longitud total −0.3 %. Sin simplificar, Miraflores parece 29 % más denso que SJM (1 150 vs 889 nodos/km²); simplificado, 416 vs 425.

**Datos faltantes en el grafo limpio** (`data/processed/datos_faltantes_por_distrito.csv`, figura `hito1_08`):

| Atributo sin dato | Miraflores | SJM | Total |
|---|---:|---:|---:|
| `name` | 42.9 % | 57.2 % | 51.8 % |
| `maxspeed` | 50.2 % | 87.9 % | 76.3 % |
| `lanes` | 50.7 % | 77.6 % | 69.3 % |

Tratamiento: no se imputan; el análisis peatonal usa velocidad de caminata constante y estos atributos no intervienen.

## 2. Limpieza (3.1) – `data/processed/limpieza_registro.csv`

| Etapa | Nodos | Aristas | Componentes |
|---|---:|---:|---:|
| Grafo crudo | 17 834 | 52 768 | 112 |
| Componente principal por distrito | 17 265 | 51 638 | 2 |
| Sin bucles (70) ni paralelas (352) | 17 265 | 51 216 | 2 |

Proyección a EPSG:32718 validada: la longitud de la geometría proyectada coincide con `length` (razón 0.995–1.001). Grafo final: Miraflores 3 841 nodos, SJM 9 127, buffer 4 297 (usado solo para el ruteo).

## 3. POI (3.1 y 3.2) – `data/processed/poi_resumen.csv`, `poi_snap.csv`

| Capa | Brutos | Únicos | En alcance del grafo | Válidos (snap ≤ 100 m) |
|---|---:|---:|---:|---:|
| Salud | 126 | 126 | 74 | 74 |
| Educación | 748 | 734 | 412 | 407 |
| Mercados | 205 | 203 | 102 | 102 |

Distancia de snap (588 POI en alcance): mediana 29.3 m, percentil 90 56.3 m, máximo 255 m. Salud: 65 clínicas, 8 hospitales y 1 `centre`. Los POI de la zona ampliada (475 de 1 063) quedan fuera del grafo (efecto de borde).

## 4. Construcción de la red (3.2) – `02c`, `src/red.py`

Grafo simple (sin bucles ni paralelas), **simétrico** (100 % de las aristas tiene inversa con la misma longitud): `DiGraph` con 17 265 nodos y 51 216 aristas dirigidas; vista no dirigida con 25 608 aristas y 2 componentes. Peso: `tiempo_min = longitud / 80 m/min` (4.8 km/h); 5, 10 y 15 min equivalen a 400, 800 y 1 200 m. Los 583 POI válidos están en 527 nodos distintos.

## 5. Exploración espacial (secciones 3.3 y 4) – `data/processed/eda_comparacion_distritos.csv`

| Métrica (por distrito) | Miraflores | SJM |
|---|---:|---:|
| Nodos / km² | 407 | 414 |
| Intersecciones (grado ≥ 3) / km² | 341 | 377 |
| km de vía / km² | 28.5 | 29.2 |
| Longitud media de arista (m) | 47.1 | 46.4 |
| % de nodos sin salida | 14.6 | 8.4 |
| % longitud arterial / local / peatonal / escaleras | 25.8 / 46.9 / 27.1 / 0.2 | 17.6 / 61.2 / 16.3 / 4.9 |
| Entropía de orientación H (nats) / índice de orden φ | 3.41 / 0.15 | 3.52 / 0.06 |
| POI por km²: educación / mercados / salud | 6.7 / 3.2 / 3.2 | 12.9 / 2.3 / 1.1 |
| % del área sin red (celdas de 100 m) | 3.5 | 6.8 |

## 6. Métricas globales y locales (3.3 y 4) – `data/processed/metricas_globales.csv`, `metricas_nodos.csv`

Subgrafos por distrito (componente gigante: 3 810 y 9 103 nodos, el 99.2 % y 99.7 %).

| Métrica | Miraflores | SJM |
|---|---:|---:|
| Aristas (calles no dirigidas) | 5 587 | 13 737 |
| Grado medio ⟨k⟩ / máximo | 2.93 / 7 | 3.02 / 6 |
| Agrupamiento medio C (aleatorio ⟨k⟩/N) | 0.047 (0.0008) | 0.024 (0.0003) |
| Longitud media de camino (m / saltos) | 2 172 / 34.8 | 3 553 / 48.9 |
| L aleatoria ln N / ln⟨k⟩ (saltos) | 7.7 | 8.3 |
| Diámetro (m / saltos) | 7 562 / 107 | 11 485 / 141 |
| Circuity: todos los pares / pares a ≤ 1 200 m | 1.18 / 1.26 | 1.25 / 1.37 |
| Eficiencia global relativa | 0.80 | 0.77 |

**Lectura con la teoría del curso:** red espacial planar sin hubs (grado casi constante, máx. 7 y 6); no es de mundo pequeño (caminos 4.5–5.9 veces más largos que en un grafo aleatorio equivalente, con agrupamiento 62–72 veces mayor: estructura regular tipo malla); en trayectos cortos el rodeo es mayor (circuity 1.26 y 1.37), de modo que 1 200 m por la red equivalen a unos 950 m (Miraflores) y 880 m (SJM) en línea recta.

**Centralidades:** cercanía exacta; intermediación aproximada con `k = 500`, ponderada por longitud, semilla 42; PageRank sin pesos. La cercanía y la intermediación no son comparables en valor absoluto entre distritos (dependen del tamaño de la red). La intermediación se concentra en pocos ejes arteriales (mediana 0.004 / 0.002; máximo 0.14 / 0.18).

**Error de la intermediación aproximada** (contra la exacta de Miraflores, `metricas_error_betweenness.csv`):

| k | Spearman | Jaccard del top 5 % | Error medio / máximo |
|---:|---:|---:|---:|
| 100 | 0.973 | 0.854 | 1.7 % |
| 250 | 0.981 | 0.891 | 1.1 % |
| 500 | 0.989 | 0.910 | 0.7 % |
| 1000 | 0.995 | 0.939 | 0.5 % |

El error se midió solo en Miraflores; en SJM, `k = 500` es el 5.5 % de los nodos y podría ser algo mayor.

## 7. Isócrona de prueba (adelanto del Hito 2) – figura `hito1_09`

Hospital Central FAP (borde norte de Miraflores): 105 nodos a 5 min, 272 a 10 min y 634 a 15 min (3.7 % del grafo). De los 362 nodos alcanzados entre 10 y 15 min, 253 (70 %) caen en el buffer. El resultado por tiempo coincide exactamente con el cálculo por longitud (400, 800 y 1 200 m).

## 8. Limitaciones a declarar (sección 5)

1. **Efecto de borde:** el grafo llega solo a 300 m de los distritos; la isócrona de ejemplo se trunca en ese límite. Nota y criterio de decisión en `docs/hito2/01_nota_ampliar_grafo.md`.
2. **Velocidad constante** de 4.8 km/h: sin pendiente (SJM tiene laderas y 4.9 % de escaleras) ni cruces.
3. **Completitud de OSM:** hasta el 88 % de las aristas de SJM sin `maxspeed`; posibles vacíos de equipamiento o de red (3.5 % y 6.8 % del área sin red).
4. **Dos redes independientes:** los distritos no son contiguos; no se analiza el paso de uno a otro.
5. **Conteos de equipamiento no son acceso:** sin población no se puede afirmar qué distrito está mejor servido (Hito 2).
6. **Pocos hospitales** en OSM (8 válidos); el análisis de salud incluye clínicas.
7. **OSM cambia:** dos descargas con 1.5 h de diferencia difirieron en 47 nodos del buffer.
8. **Intermediación aproximada:** error medido solo en Miraflores.

## 9. Correspondencia con la plantilla del artículo

| Sección | Material |
|---|---|
| 1. Introducción, 2. Marco teórico | Teoría del curso; ver referencias sugeridas abajo |
| 3.1 Datos | §1 y §2 de este resumen; `hito1_01_area_estudio`, `hito1_08_datos_faltantes`, `hito1_10_efecto_simplify` |
| 3.2 Construcción de la red | §4; `docs/hito1/06_construccion_red.md` |
| 3.3 Análisis y métricas | §5 y §6 |
| 3.4 Herramientas | `requirements.txt`, `docs/hito1/10_pipeline_metodologico.md`, `hito1_11_pipeline` |
| 4. Resultados | `eda_01`–`eda_05`, `metricas_01`–`metricas_03`, `hito1_09_isocrona_prueba`; pies de figura en `figures/CATALOGO.md` |
| 5. Discusión | §6 (lectura con la teoría) y §8 (limitaciones) |
| 6. Conclusiones, 7. Referencias, 8. Anexos | Consulta y fecha de descarga en los logs de `data/raw/`; atribución a OpenStreetMap |

## 10. Referencias sugeridas

Son obras conocidas relacionadas con lo que se usó; **verificar los datos de cada una antes de citarlas** (no se consultaron en línea).

- Barthélemy, M. (2011). Spatial networks. *Physics Reports, 499*(1–3), 1–101.
- Boeing, G. (2017). OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. *Computers, Environment and Urban Systems, 65*, 126–139.
- Boeing, G. (2019). Urban spatial order: Street network orientation, configuration, and entropy. *Applied Network Science, 4*, 67.
- Brandes, U. (2001). A faster algorithm for betweenness centrality. *Journal of Mathematical Sociology, 25*(2), 163–177.
- Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). Exploring network structure, dynamics, and function using NetworkX. *Proceedings of the 7th Python in Science Conference*, 11–15.
- Latora, V., & Marchiori, M. (2001). Efficient behavior of small-world networks. *Physical Review Letters, 87*(19), 198701.
- Porta, S., Crucitti, P., & Latora, V. (2006). The network analysis of urban streets: A primal approach. *Environment and Planning B, 33*(5), 705–725.
- Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of "small-world" networks. *Nature, 393*, 440–442.
- OpenStreetMap contributors. (2026). *OpenStreetMap* [Base de datos]. https://www.openstreetmap.org (licencia ODbL). **Atribución obligatoria.**
