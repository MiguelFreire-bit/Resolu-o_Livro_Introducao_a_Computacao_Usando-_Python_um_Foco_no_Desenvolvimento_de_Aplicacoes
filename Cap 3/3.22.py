lista = []
while lista.count("pare") != 1:
    x = input("digite um elemento da lista ")
    lista.append(x)

print("\n")
lista.remove("pare")
for i in lista:
    if i != "segredo":
        print(i)

