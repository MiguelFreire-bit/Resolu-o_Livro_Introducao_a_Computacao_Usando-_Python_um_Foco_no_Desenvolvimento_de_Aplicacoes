def particao_jogadores(jogadores):
    for jogador in jogadores:
        if jogador[0].upper() >= 'A' and jogador[0].upper() <= 'M':
            print(jogador)
particao_jogadores(['Elano', 'Edinho', 'silas', 'obina', 'gerson'])