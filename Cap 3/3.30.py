#peguei no chatGPT
while True:
    numero = int(input("Digite um número de 4 dígitos: "))

    if len(str(numero)) == 4:
        # resto de numero dividido por dez
        digito_4 = numero % 10
        # (divisão inteira de numero por ), resto de resultado do () por
        digito_3 = (numero // 10) % 10
        digito_2 = (numero // 100) % 10
        digito_1 = (numero // 1000) % 10

        print(digito_1)
        print(digito_2)
        print(digito_3)
        print(digito_4)
        break