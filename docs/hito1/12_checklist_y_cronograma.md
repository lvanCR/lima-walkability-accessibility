# Paso 12 – Checklist contra la rúbrica

Estado al cierre del trabajo técnico del Hito 1. `[x]` = hecho y verificado; `[ ]` = pendiente (indicando de quién). Se apunta la evidencia de cada punto.

## Construcción y calidad del dato (15 %)
- [x] Área justificada: `01_area_estudio.md`, figura `hito1_01_area_estudio`.
- [x] Grafo ≥ 3 000 nodos y ≥ 6 000 aristas: 17 265 nodos y 51 216 aristas (`01`, verificación final con `assert`).
- [x] `network_type='walk'` justificado: `01_area_estudio.md` y `02c`.
- [x] Proyección a EPSG:32718 verificada: razón longitud proyectada / `length` entre 0.995 y 1.001 (`01`).
- [x] Capa de POI integrada al grafo: 583 POI en 527 nodos (`02b`, `02c`).
- [x] Limpieza documentada (antes → después): `data/processed/limpieza_registro.csv`.

## Rigor en el análisis de red (30 %)
- [x] Métricas globales y locales: `03` sección 8; tablas en `data/processed/metricas_*.csv`.
- [x] Normalización por área o nº de nodos: `03` sección 3 y `eda_comparacion_distritos.csv`. Las centralidades de cercanía e intermediación dependen del tamaño y se comparan por patrón, no por valor (declarado).
- [x] Intermediación aproximada: `k = 500`, semilla 42, ponderada por longitud y error medido contra la exacta (Spearman 0.989).
- [x] Efecto de `simplify=True` explicado con una descarga sin simplificar: sección final de `01`, `data/raw/simplify_comparacion.json`.
- [x] Porcentaje de datos faltantes reportado y tratamiento explicado: `hito1_08_datos_faltantes`, `datos_faltantes_por_distrito.csv`.
- [x] Validaciones: tiempo vs. longitud en `02c`; cobertura de ambos distritos y recarga del grafo en `01`.

## Visualización y cartografía (15 %)
- [x] Mapas con escala, norte, leyenda y fuente (`src/mapas.py`); 11 figuras a 200 dpi (comprobado en `03b`).
- [x] Pie de figura interpretativo para cada una: `figures/CATALOGO.md`.
- [ ] Legibilidad en escala de grises: **no se verificó** (paletas usadas: viridis, YlOrRd, rojo-amarillo-verde en la isócrona, y categóricas para tipo de vía).

## Interpretación y explicabilidad (20 %)
- [x] Hallazgos conectados con la teoría del curso (redes espaciales planares, ausencia de hubs, mundo pequeño, circuity, eficiencia): notebooks `03` y `13_resumen_de_resultados.md`.
- [x] Limitaciones declaradas: efecto de borde, velocidad constante, completitud de OSM, dos redes independientes, intermediación aproximada (`13_resumen_de_resultados.md` §8).
- [ ] Redacción de la discusión en el informe: **a cargo del equipo**.

## Reproducibilidad y código (10 %)
- [x] Entorno documentado con versiones exactas: `requirements.txt`.
- [x] Semilla fija (42) en `src/config.py`.
- [x] Grafo exportado con fecha, consulta, versiones y SHA-256: `data/raw/*_log.json`.
- [x] Código reutilizable en `src/` y parámetros en un único archivo (`config.py`).
- [x] Ejecución desde cero en un entorno limpio: ver la sección «Verificación de reproducibilidad» más abajo.
- [ ] Subir el repositorio a GitHub (`git push`) y compartirlo con el docente: **a cargo del equipo** (todos los commits están en local).
- [ ] El notebook `01` mezcla celdas de Colab (descarga) y locales (limpieza): documentado en `README.md` y en el pipeline; si el docente exige un notebook que corra de principio a fin sin Colab, habría que ejecutarlo en Colab completo.

## Comunicación (10 %)
- [ ] Exposición de 10 min: **a cargo del equipo**.
- [ ] Video de 10 min: **a cargo del equipo**.
- Material de apoyo: `figures/CATALOGO.md`, `docs/hito1/13_resumen_de_resultados.md` y `figures/plots/hito1_11_pipeline.png`.

---

## Pendientes antes de entregar

1. Confirmar en el aula virtual que el área (Miraflores + San Juan de Miraflores) no está asignada a otro grupo.
2. Redactar el informe del Hito 1 (plantilla del enunciado) en `reports/hito1/`.
3. Preparar la exposición y grabar el video.
4. `git push` y dar acceso al docente.
5. Repartir responsabilidades y fechas entre los tres integrantes (tabla siguiente).

## Cronograma y responsables (por completar por el equipo)

| Etapa | Responsable | Fecha |
|---|---|---|
| Confirmación del área | | |
| Informe del Hito 1 | | |
| Diapositivas y exposición | | |
| Video | | |
| Push del repositorio y acceso al docente | | |

---

## Verificación de reproducibilidad

Se hizo en una **copia limpia del repositorio y un entorno virtual nuevo** (Python 3.12.2) con `pip install -r requirements.txt` (versiones exactas):

- Los notebooks `02b`, `02c`, `03` y `03b` se ejecutaron de principio a fin sin errores (unos 2.5 minutos en total).
- La sección de carga, inventario, limpieza y comparación de `simplify` de `01` se volvió a ejecutar partiendo del grafo crudo: el grafo limpio se regeneró con los mismos 17 265 nodos y 51 216 aristas, y `limpieza_registro.csv` salió idéntico.
- Las siete tablas de resultados (`poi_snap`, `poi_resumen`, `metricas_globales`, `metricas_nodos`, `metricas_error_betweenness`, `eda_comparacion_distritos` y `datos_faltantes_por_distrito`) salieron **idénticas** a las del repositorio (comparación con 6 decimales), lo que confirma que la semilla fija y el entorno bastan para reproducir los números.

**Alcance:** se partió de los archivos descargados de OSM guardados en `data/raw`. No se repitieron las descargas (`01` celdas de descarga, `01b`, `02a`), que requieren Overpass y devolverían datos distintos si OSM cambió; para eso están el log y el hash de cada archivo.
