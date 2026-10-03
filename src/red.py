"""Construcción del grafo ponderado para el análisis de accesibilidad peatonal."""
import networkx as nx


def metros_por_minuto(velocidad_kmh):
    """Velocidad de caminata en km/h -> metros por minuto."""
    return velocidad_kmh * 1000 / 60


def construir_digrafo(G, velocidad_kmh):
    """Grafo limpio (MultiDiGraph sin aristas paralelas) -> DiGraph simple.

    Cada arista recibe `tiempo_min` = longitud (m) / velocidad (m/min). Los atributos
    de nodos y aristas se conservan.
    """
    if any(len(G[u][v]) > 1 for u, v in G.edges()):
        raise ValueError("Quedan aristas paralelas: limpiar el grafo antes de ponderarlo")
    D = nx.DiGraph(G)
    mpm = metros_por_minuto(velocidad_kmh)
    for _, _, d in D.edges(data=True):
        d["tiempo_min"] = d["length"] / mpm
    return D
