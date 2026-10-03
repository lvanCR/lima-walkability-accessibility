# Paso 4 – Limpieza y proyección

**Notebook:** `01_descarga_y_limpieza`

## Objetivo
Dejar un grafo consistente, conectado y en CRS métrico, y documentar cada decisión.

## Tareas
1. **Simplificación:** el grafo ya viene con `simplify=True`. Documentar el efecto comparando con una descarga sin simplificar (conteo de nodos antes/después, como pide el enunciado). Si es costoso, hacerlo solo en el distrito más pequeño (Miraflores) y extrapolar con cuidado.
2. **Componentes conexos:** calcular componentes (débiles/fuertes); conservar el componente gigante y reportar cuántos nodos/aristas se descartan y dónde están (mapa).
3. **Atributos:**
   - normalizar atributos tipo lista (elegir un criterio, p. ej. primer valor o el de mayor jerarquía),
   - decidir tratamiento de `maxspeed`/`lanes`/`name` faltantes: **no se imputan** para el análisis peatonal (la velocidad de caminata es constante); solo se reportan,
   - verificar longitudes (`length`) no nulas ni cero.
4. **Aristas atípicas:** revisar bucles, aristas muy cortas (< 1 m) y muy largas (outliers).
5. **Proyección:** `ox.project_graph(G, to_crs='EPSG:32718')`. Verificar que todas las distancias se calculan en metros.
6. **Etiqueta de distrito:** asignar a cada nodo su distrito (Miraflores / SJM) con join espacial.
7. **Exportación:** guardar el grafo limpio en `data/interim/` (GraphML) y nodos/aristas en GeoPackage (`data/processed/`).

## Registro obligatorio
Una tabla "Antes → Después" con nodos, aristas, componentes y datos descartados, y la razón de cada descarte.

## Criterio de aceptación
Grafo de un solo componente (o justificación documentada), todo en EPSG:32718, con ≥ 3 000 nodos y ≥ 6 000 aristas.

## Resultado sobre `simplify=True`

Medido con una descarga sin simplificar de la misma zona (`01b_efecto_simplify_colab`, resultado en `data/raw/simplify_comparacion.json`): los nodos pasan de 42 545 a 17 787 (−58.2 %) y las aristas de 102 158 a 52 642 (−48.5 %); se eliminan casi todos los nodos de geometría y se conservan las intersecciones y la longitud total de vía. El conteo sin simplificar no es comparable entre distritos (Miraflores parece 29 % más denso; simplificado, la razón es 0.98). Detalle y conclusiones en la sección final de `01_descarga_y_limpieza`.

## Estado

Completado en `01`. Decisión: los nodos del buffer no se recortan; se etiquetan `Fuera (buffer)` y se usan solo para el ruteo, para limitar el efecto de borde. Registro en `data/processed/limpieza_registro.csv`.
