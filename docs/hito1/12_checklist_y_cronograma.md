# Paso 12 – Checklist contra la rúbrica y cronograma

## Checklist por criterio (aplicado al Hito 1)

### Construcción y calidad del dato (15 %)
- [ ] Área justificada.
- [ ] Grafo ≥ 3 000 nodos y ≥ 6 000 aristas.
- [ ] `network_type='walk'` justificado.
- [ ] Proyección a EPSG:32718 verificada.
- [ ] Al menos una capa de POI/polígonos integrada al grafo.
- [ ] Limpieza documentada (antes/después).

### Rigor en el análisis de red (30 %)
- [ ] Métricas globales y locales calculadas correctamente.
- [ ] Normalización por área o nº de nodos.
- [ ] Betweenness aproximada: `k` declarado, semilla fija y discusión del error.
- [ ] Efecto de `simplify=True` explicado.
- [ ] Porcentaje de datos faltantes reportado y tratamiento explicado.

### Visualización y cartografía (15 %)
- [ ] Mapas con escala, norte, leyenda y fuente.
- [ ] Paletas coherentes.
- [ ] Pie de figura interpretativo.

### Interpretación y explicabilidad (20 %)
- [ ] Hallazgos conectados con la teoría del curso (redes espaciales, planaridad, ausencia de hubs, small-world).
- [ ] Limitaciones declaradas (topografía, completitud OSM, efecto de borde).

### Reproducibilidad y código (10 %)
- [ ] Notebooks ejecutables de principio a fin.
- [ ] `requirements.txt` actualizado con versiones.
- [ ] Semilla fija.
- [ ] Grafo exportado + log + hash.
- [ ] Repositorio Git compartido con el docente.

### Comunicación (10 %)
- [ ] Exposición de 10 min ensayada.
- [ ] Video de 10 min grabado.

## Cronograma (fechas por definir con el calendario del curso)
| Etapa | Pasos | Responsable | Fecha |
|---|---|---|---|
| Preparación y confirmación del área | 1 | | |
| Descarga y limpieza | 2–4 | | |
| POI y construcción de la red | 5–6 | | |
| EDA y métricas | 7–8 | | |
| Mapas y figuras | 9 | | |
| Pipeline, diapositivas y guion | 10–11 | | |
| Video y entrega | 11–12 | | |

> Completar responsables y fechas una vez conocida la fecha de entrega del Hito 1.
