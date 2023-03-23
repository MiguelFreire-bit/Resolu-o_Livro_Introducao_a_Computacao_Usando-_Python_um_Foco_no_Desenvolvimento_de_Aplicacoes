import numpy as np

lista = []
while len(lista) < 4:
    n = eval(input("digite n: "))
    if type(n) == int or type(n) == float:
        lista.append(n)
print(lista)


media = np.mean(lista[0:3])
print(media)
if media == lista[3]:
    print("igual")



