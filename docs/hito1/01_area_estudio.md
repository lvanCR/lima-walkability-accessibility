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
- [ ] Obtener polígonos de límites distritales (OSM vía `geocode_to_gdf`) y confirmar que coinciden con el límite oficial.
- [ ] Decidir si el análisis trata los dos distritos como un solo grafo o como dos subgrafos comparables (propuesta: un solo grafo descargado con límite unido, y etiqueta de distrito por nodo).
