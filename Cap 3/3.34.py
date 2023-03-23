def inverte_int(a):
    while True:
        int(a)
        if 100 <= a <= 999 and a % 10 != 0:
            x = a % 10
            y = (a // 10) % 10
            z = a // 100
            novo_num = x * 100 + y * 10 + z
            print(novo_num)
            break
        else:
            a = int(input("escreva um número válido: "))
inverte_int(12)