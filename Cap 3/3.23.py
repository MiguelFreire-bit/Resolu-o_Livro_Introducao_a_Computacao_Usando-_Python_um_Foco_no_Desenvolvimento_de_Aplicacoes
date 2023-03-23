lista = []
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
while lista.count("pare") != 1:
    x = input("digite a lista: ")
    lista.append(x)

print("\n")
lista.remove("pare")
for i in lista:
    if letras.count(i[0]) == 1:
        print(i)