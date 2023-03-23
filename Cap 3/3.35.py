import numpy as np


def pontos(x1, y1, x2, y2):
    ponto_1 = [x1, y1]
    ponto_2 = [x2, y2]

    if x1 == x2:
        distancia_1 = str(np.sqrt((x2 - x1) **2 + (y2 - y1) **2))
        print(f"a inclinação é infinita e a distância é: {distancia_1}")
    else:
        distancia_1 = str(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        angulo = str(((y2 - y1) / (x2 - x1)))
        print(f"a inclinação é {angulo} e a distância é: {distancia_1}")
pontos(0, 0, 1, 1)