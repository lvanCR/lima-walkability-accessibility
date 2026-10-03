# lima-walkability-accessibility

**Accesibilidad peatonal a equipamiento urbano en Lima (Miraflores + San Juan de Miraflores) mediante isócronas.**

Curso Complex Networks, UPC 2026-2. Isócronas peatonales (5/10/15 min) desde hospitales, colegios y mercados sobre el grafo vial de OpenStreetMap.

## Estructura
- `data/raw|interim|processed`: datos (grafo GraphML/GeoPackage, POI)
- `notebooks/`: flujo 01→05 (descarga, POI, métricas, isócronas, comparación)
- `src/`: configuración y funciones reutilizables
- `figures/`: mapas y gráficos
- `reports/hito1|hito2`: artículo y material del parcial / final
- `video/`: videos de exposición

## Pendientes
- [ ] Área de estudio asignada (editar `src/config.py`)
- [ ] Entorno: `pip install -r requirements.txt` (rtree requiere libspatialindex)
- [ ] Repositorio Git compartido con el docente

Datos © OpenStreetMap contributors (ODbL).
