def abreviação (x):
    while True:
        if type(x) == str:
            print(x[0:3])
            break
        else:
            x = input("escreva o dia da semana: ")

abreviação('terça-feira')