def ion2e(x):
    if x[-3:] == 'ion':
        y = x[:-3] + "e"
        print(y)
    else:
        print(x)

ion2e('congratulation')

#Sua solução está quase correta, mas é preciso fazer alguns ajustes.
# Em vez de usar a instrução break, que é usada para interromper loops,
# você pode simplesmente retornar o valor correto da palavra. Além disso,
# em vez de imprimir o valor retornado, você deve retornar o valor para que
# ele possa ser usado em outras partes do código. Por fim, é melhor não usar
# um print dentro da função, mas sim um return.

#sugestão de código chatGPT:

def ion2e_(x):
    if x.endswith('ion'):
        return x[:-3] + 'e'
    else:
        return x

print(ion2e_('congratulation'))