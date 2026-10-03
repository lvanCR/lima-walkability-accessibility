# Paso 1 – Definición y justificación del área de estudio

## Objetivo
Dejar por escrito qué territorio se analiza y por qué es pertinente para el tema de accesibilidad peatonal a equipamiento urbano.

## Área elegida
**Miraflores + San Juan de Miraflores (SJM)**, Lima Metropolitana.

## Justificación (borrador)
- **Contraste socioeconómico y morfológico:** Miraflores es un distrito consolidado y plano; SJM combina zonas consolidadas con laderas de cerro y crecimiento informal. Esto permite el contraste que pide el tema.
- **Tamaño adecuado:** ≈12 900 nodos entre ambos, dentro del rango 3 000–60 000. Permite cálculos de centralidad factibles en clase.
- **Equipamiento:** ambos distritos tienen hospitales, colegios y mercados en OSM (por verificar cantidades en el paso 5).
- **Contexto de datos abiertos:** hay censo INEI, registro de colegios (MINEDU/ESCALE) y de establecimientos de salud (SUSALUD/MINSA) para contrastar los POI de OSM.

## Justificación del `network_type`
- `'walk'`: el tema exige red peatonal. En osmnx incluye calles, veredas, escaleras y pasajes peatonales, y no respeta el sentido de las vías vehiculares.

## Riesgos a documentar
- **Topografía:** SJM tiene cerros; la velocidad de caminata real baja en pendiente y el modelo no la considera. Limitación a declarar.
- **Completitud de OSM:** puede ser menor en zonas informales de SJM (escaleras, pasajes).
- **Efectos de borde:** al recortar por distrito se cortan rutas hacia POI fuera del límite. Evaluar un buffer alrededor del límite al descargar.
- **Tamaño de Miraflores:** 3 828 nodos pasa el mínimo con poco margen; verificar tras la limpieza.

## Entregable del paso
Sección "Área de estudio" para la presentación y para el artículo (3.1 Datos).

## Pendiente
- [x] Obtener polígonos de límites distritales (OSM vía `geocode_to_gdf`). La comparación con el límite oficial no se hizo; las áreas obtenidas son 9.45 km² (Miraflores) y 22.06 km² (SJM).
- [x] Decidir si el análisis trata los dos distritos como un solo grafo o como dos subgrafos: se descargan en una sola consulta y se analizan como **dos redes independientes**, con etiqueta de distrito por nodo (ver «Estado»).

## Estado

Completado. **Decisión final:** Miraflores y San Juan de Miraflores no son contiguos (Surco queda entre ambos), por lo que se tratan como **dos redes independientes** (un componente por distrito), descargadas en una sola consulta con `retain_all=True` y analizadas por distrito. La propuesta inicial de un solo grafo conectado quedó descartada al comprobar que `retain_all=False` descartaba Miraflores entera. Mapa en `figures/maps/hito1_01_area_estudio.png`. Pendiente por el equipo: confirmar en el aula virtual que el área no está asignada a otro grupo.
