s = 'boi'

value = input('Escreva uma string de três letras:')
while (len(value) != 3):
    value = input('Escreva uma string de três letras:')
if value[0] == s[-1] and value[1] == s[-2] and value[2] == s[-3]:
    print('igual ao inverso!!')
else:
    print('diferente!')


