# Paso 9 – Mapas y visualizaciones preliminares

**Notebook:** `03_metricas_y_eda`

## Estándar cartográfico (se evalúa el 15 %)
Cada mapa debe tener: **escala, flecha de norte, leyenda, título, paleta adecuada, fuente (© OpenStreetMap contributors)**. Usar EPSG:32718 y, si se usa mapa base, `contextily`.

## Lista mínima de figuras
| # | Figura | Tipo |
|---|---|---|
| 1 | Área de estudio con límites distritales | Mapa |
| 2 | Red peatonal con tipo de vía | Mapa |
| 3 | POI sobre la red (hospitales, colegios, mercados) | Mapa |
| 4 | Betweenness (o closeness) por nodo/arista | Mapa |
| 5 | Histograma de longitud de aristas por distrito | Gráfico |
| 6 | Distribución de grado | Gráfico |
| 7 | Diagrama polar de orientación de calles por distrito | Gráfico |
| 8 | Datos faltantes por atributo | Gráfico/tabla |
| 9 (opcional) | Isócrona de prueba desde un POI | Mapa |

## Guía de estilo
- Misma paleta y tipografía en todas las figuras; usar paletas secuenciales para centralidades y categóricas para tipo de vía.
- Evitar arco iris; verificar legibilidad en escala de grises.
- Cada figura debe responder a una pregunta y tener un pie de figura que la interprete.
- Guardar en `figures/maps/` y `figures/plots/` con resolución suficiente para diapositivas (≥ 200 dpi).

## Entregable
Figuras finales numeradas y con pie de figura listo para el artículo y la presentación.
