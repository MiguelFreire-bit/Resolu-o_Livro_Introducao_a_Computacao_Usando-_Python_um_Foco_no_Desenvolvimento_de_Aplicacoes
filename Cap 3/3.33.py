def prob(a):
    while True:
        if a < 0:
            a = int(input("escreva um inteiro positivo: "))
        else:
            print(2 ** (-a))
            break


prob(2)
