# Solicitando ao usuário um inteiro positivo de 3 dígitos
num = int(input("Digite um número de 3 dígitos: "))

# Extraindo o primeiro dígito
primeiro = num // 100

# Extraindo o segundo dígito
segundo = (num // 10) % 10

# Extraindo o terceiro dígito
terceiro = num % 10

# Exibindo os dígitos
print(primeiro)
print(segundo)
print(terceiro)
