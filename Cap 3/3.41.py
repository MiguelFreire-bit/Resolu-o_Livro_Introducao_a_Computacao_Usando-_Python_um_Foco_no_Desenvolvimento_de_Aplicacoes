import numpy as np


def acerto(xc, yc, r, xp, yp):
    """
    Verifica se um ponto (xp, yp) está dentro ou sobre um círculo de centro (xc, yc) e raio r.

    Args:
    xc (float): coordenada x do centro do círculo
    yc (float): coordenada y do centro do círculo
    r (float): raio do círculo
    xp (float): coordenada x do ponto
    yp (float): coordenada y do ponto

    Returns:
    bool: True se o ponto está dentro ou sobre o círculo, False caso contrário
    """
    d = np.sqrt((xp - xc) ** 2 + (yp - yc) ** 2)
    return d <= r

print(acerto(0, 0, 3, 3, 0))