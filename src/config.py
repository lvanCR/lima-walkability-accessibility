"""Parámetros globales del proyecto."""
from pathlib import Path

SEED = 42
ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_INTERIM = ROOT / "data" / "interim"
DATA_PROCESSED = ROOT / "data" / "processed"
FIG_MAPS = ROOT / "figures" / "maps"
FIG_PLOTS = ROOT / "figures" / "plots"

PLACES = ["Miraflores, Lima, Peru", "San Juan de Miraflores, Lima, Peru"]
BUFFER_M = 300          # buffer alrededor del límite para reducir efecto de borde
NETWORK_TYPE = "walk"   # tema 4 exige red peatonal
CRS_METRIC = "EPSG:32718"  # UTM 18S (Lima); ajustar si es otra ciudad
WALK_SPEED_KMH = 4.8
ISOCHRONE_MINUTES = [5, 10, 15]
POI_TYPES = ["hospital", "school", "marketplace"]
DISTRICT_LABELS = ["Miraflores", "San Juan de Miraflores"]

POI_BUFFER_M = 1200      # zona ampliada de descarga de POI (15 min a pie)
SNAP_MAX_M = 100        # POI a más de esta distancia de su nodo más cercano se marcan como no válidos
DEDUP_M = 100           # radio para considerar duplicado un POI con el mismo nombre
