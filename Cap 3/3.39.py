def invert (nome_completo):
    espaco_branco = nome_completo.index(" ")
    sobrenome = nome_completo[espaco_branco+1:]
    print(f'{sobrenome.capitalize()}, {nome_completo[0].upper()}')
    
invert('miguel freire')
