# Hito 1 (Parcial, EA1) – Índice y alcance

**Proyecto:** Accesibilidad a equipamiento urbano mediante áreas de servicio (Tema 4)
**Área de estudio:** Miraflores + San Juan de Miraflores (Lima Metropolitana)
**Red:** peatonal (`network_type='walk'`)

## Qué pide el Hito 1 (según el enunciado)

1. Definición y justificación del área de estudio.
2. Descarga y limpieza del grafo.
3. Análisis exploratorio espacial.
4. Primeras métricas globales y locales.
5. Mapas y visualizaciones preliminares.
6. Pipeline metodológico.
7. Exposición en clase (10 min) y video (10 min) con hallazgos preliminares.

## Qué queda FUERA del Hito 1 (es del Hito 2)

- Cálculo completo de isócronas 5/10/15 min y cobertura final.
- Comparación socioeconómica con validación.
- Artículo científico completo.

> Se puede mostrar una isócrona de prueba desde un solo POI como adelanto, pero no es obligatoria.

## Pasos (un archivo por paso)

| # | Archivo | Notebook asociado | Salida principal |
|---|---|---|---|
| 1 | `01_area_estudio.md` | – | Justificación del área |
| 2 | `02_descarga_datos.md` | `01_descarga_y_limpieza` | Grafo crudo en disco + registro de reproducibilidad |
| 3 | `03_carga_y_estructura.md` | `01_descarga_y_limpieza` | Inventario del grafo (nodos, aristas, atributos) |
| 4 | `04_limpieza.md` | `01_descarga_y_limpieza` | Grafo limpio y proyectado a EPSG:32718 |
| 5 | `05_poi_y_capas.md` | `02_poi_y_capas` | POI integrados al grafo |
| 6 | `06_construccion_red.md` | `01`/`02` | Definición formal del grafo y ponderación |
| 7 | `07_eda_espacial.md` | `03_metricas_y_eda` | Exploración espacial y de atributos |
| 8 | `08_metricas.md` | `03_metricas_y_eda` | Tabla de métricas globales y locales |
| 9 | `09_mapas_y_visualizaciones.md` | `03_metricas_y_eda` | Mapas y gráficos preliminares |
| 10 | `10_pipeline_metodologico.md` | – | Diagrama y descripción del pipeline |
| 11 | `11_exposicion_y_video.md` | – | Guion, diapositivas y video |
| 12 | `12_checklist_y_cronograma.md` | – | Checklist contra la rúbrica |

## Decisiones ya tomadas

- Área: Miraflores + San Juan de Miraflores (contraste socioeconómico).
- Tamaño verificado con prueba de descarga (`walk`, `simplify=True`): Miraflores 3 828 nodos, SJM 9 106 nodos (≈12 900 en total, dentro del rango 3 000–60 000).
- Entorno: venv `D:\Topicos de computacion\.venv` (Python 3.12, osmnx 2.1.1, geopandas 1.2.0, rtree 1.4.1).

## Pendientes antes de empezar

- [ ] Confirmar en el aula virtual que el área no esté tomada por otro grupo.
- [ ] Repositorio Git compartido con el docente.
- [ ] Repartir responsabilidades entre los 3 integrantes.
