def med (notas_alunos):
    for nota in notas_alunos:
        media = sum(nota) / len(nota)
        print(media)

med([[95,92,86,87], [66,54], [89,72,100], [33,0,0]])