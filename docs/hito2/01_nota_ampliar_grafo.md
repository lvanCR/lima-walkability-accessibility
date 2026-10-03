# Nota para el Hito 2 – ¿Ampliar el grafo más allá del buffer de 300 m?

**Estado:** abierta. Decisión del Hito 1: **mantener el grafo con buffer de 300 m**. Evaluar la ampliación en el Hito 2.

## Contexto

- El grafo peatonal se descargó con los distritos (Miraflores + San Juan de Miraflores) más un buffer de **300 m**.
- Los POI se descargaron con un buffer de **1 200 m** (distancia que se camina en 15 min a 4.8 km/h), para poder evaluar este punto.
- Al descargar, más de la mitad del equipamiento quedó en la zona ampliada (300–1 200 m), **fuera del grafo**:

| Capa | Total | Dentro de los distritos + buffer 300 m | Zona ampliada (300–1 200 m) |
|---|---:|---:|---:|
| Salud | 126 | 74 | 52 |
| Educación | 748 | 417 | 331 |
| Mercados | 205 | 102 | 103 |

(Conteos brutos, antes de deduplicar puntos/polígonos del mismo establecimiento.)

## Por qué importa

La accesibilidad de un residente cercano al límite depende también del equipamiento que está al otro lado. Con el grafo de 300 m:

- Ese equipamiento no se puede integrar al grafo (sin nodo cercano) y **no cuenta** en las isócronas.
- La cobertura de los nodos próximos al límite se **subestima** (efecto de borde).
- Las isócronas de 10 y 15 min (800 y 1 200 m) son las más afectadas: pueden cruzar el límite del grafo.

## Opción a evaluar: ampliar el grafo a 1 200 m

| | Efecto |
|---|---|
| A favor | Captura el equipamiento que realmente sirve a los residentes del borde; reduce el efecto de borde de las isócronas de 15 min. |
| En contra | Nueva descarga en Colab y repetir limpieza y POI; el área pasa de ≈ 45 a ≈ 90 km² y los nodos podrían duplicarse (de ≈ 17 000 a ≈ 35 000), todavía bajo el tope recomendado de 60 000 pero con cálculos de centralidad más pesados. Entran zonas de otros distritos (Surco, Surquillo, etc.) que no son parte del estudio. |

## Cómo decidir (propuesta)

1. Con el grafo actual, calcular la cobertura por isócronas y **medir cuántos nodos de los distritos tienen una isócrona truncada por el borde** (nodos a menos de 1 200 m del límite del grafo).
2. Hacer un análisis de sensibilidad: repetir el cálculo para los nodos a más de 1 200 m del borde (no afectados) y comparar con el total.
3. Si la diferencia en el % de cobertura es relevante (criterio sugerido: > 5 puntos porcentuales), ampliar el grafo; si no, mantener el de 300 m y documentar el efecto como limitación.

## Si se amplía: tareas

- [ ] Cambiar `BUFFER_M` a 1 200 en `src/config.py` y volver a ejecutar `01_descarga_y_limpieza` en Colab (con `retain_all=True`).
- [ ] Mantener la etiqueta `Fuera (buffer)`: las métricas por distrito siguen usando solo los nodos de cada distrito.
- [ ] Repetir la integración de POI (`02b_poi_integracion`) y las métricas.
- [ ] Actualizar los conteos de este documento y el informe (sección 3.1 Datos y limitaciones).

## Para el informe (sección 5, Discusión)

Declarar el efecto de borde como limitación (el enunciado lo pide expresamente) y describir el análisis de sensibilidad realizado.
