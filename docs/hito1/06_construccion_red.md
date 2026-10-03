# Paso 6 – Construcción formal de la red

## Objetivo
Definir sin ambigüedad qué es el grafo, para la sección 3.2 del artículo.

## Definición
- **Grafo:** G = (V, E), espacial, ponderado.
- **Nodo:** intersección o final de vía peatonal, con coordenadas (x, y) en EPSG:32718.
- **Arista:** segmento de calle/vereda/pasaje entre dos nodos, con geometría y longitud en metros.

## Dirigido o no dirigido
- osmnx devuelve un `MultiDiGraph`. Para `network_type='walk'` las calles se tratan como transitables en ambos sentidos, de modo que en la práctica el grafo es simétrico.
- **Verificar** en los datos cuántas aristas tienen su inversa y justificar la decisión (propuesta: mantener dirigido por compatibilidad con osmnx y comprobar la simetría; usar versión no dirigida donde convenga, p. ej. clustering).

## Ponderación
- **Peso principal:** longitud (m).
- **Tiempo de viaje:** `t = longitud / velocidad`, con velocidad de caminata constante de 4.8 km/h = 80 m/min.
  - 5 min → 400 m; 10 min → 800 m; 15 min → 1 200 m.
- Se justifica la velocidad constante porque OSM no trae velocidad peatonal. Limitación: no se considera pendiente ni cruces.
- Opcional (Hito 2): penalización por escaleras o cruces.

## Integración de capas
- POI → nodo más cercano (paso 5).
- Etiqueta de distrito por nodo (paso 4).

## Entregable
Texto formal (media página) y un diagrama simple nodo/arista/POI para la presentación.
