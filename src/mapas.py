"""Utilidades de cartografía: escala, flecha de norte y guardado de figuras."""
import numpy as np


def escala_y_norte(ax, longitud_m=1000, margen=0.04):
    """Agrega barra de escala (esquina inferior izquierda) y flecha de norte (superior derecha).

    Supone ejes en un CRS métrico (UTM): las unidades del eje son metros.
    """
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ancho, alto = x1 - x0, y1 - y0
    xi, yi = x0 + margen * ancho, y0 + margen * alto

    ax.plot([xi, xi + longitud_m], [yi, yi], color="k", lw=3, solid_capstyle="butt", zorder=10)
    ax.plot([xi, xi + longitud_m / 2], [yi, yi], color="w", lw=1.5, solid_capstyle="butt", zorder=11)
    texto = f"{longitud_m / 1000:g} km" if longitud_m >= 1000 else f"{longitud_m:g} m"
    ax.text(xi + longitud_m / 2, yi + 0.012 * alto, texto, ha="center", va="bottom", fontsize=9, zorder=10)

    xn, yn = x1 - margen * ancho * 1.5, y1 - margen * alto * 3.2
    ax.annotate("N", xy=(xn, yn + 0.09 * alto), xytext=(xn, yn), ha="center", va="bottom",
                fontsize=11, fontweight="bold", zorder=10,
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.5))


def guardar(fig, ruta, dpi=200):
    """Guarda la figura en `ruta` (crea la carpeta si hace falta)."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=dpi, bbox_inches="tight", facecolor="white")
    return ruta
