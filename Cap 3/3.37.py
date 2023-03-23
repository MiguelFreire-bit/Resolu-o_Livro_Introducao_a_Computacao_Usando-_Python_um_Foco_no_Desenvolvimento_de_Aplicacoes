def colisao(x1, y1, r1, x2, y2, r2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(distancia <= r1 + r2)


colisao(5,5,2,2,3,2)