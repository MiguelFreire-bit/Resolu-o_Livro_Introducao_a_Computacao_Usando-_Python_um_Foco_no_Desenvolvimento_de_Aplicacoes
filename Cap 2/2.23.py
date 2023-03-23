import random

# range( stop )
# range( [start], stop[, step] )

y = list(range(-5,5))
x = random.choices(y,weights=[1, 1, 1, 1, 1, 1, 5, 4, 3, 2], k=5)

#A função random.choices() permite o retorno de uma quantidade determinada de elementos.
# Também podemos definir a probabilidade para a repetição de cada elemento da sequência
# que servirá de base para a produção do resultado aleatório. A sintaxe do comando é:
#
# random.choices(sequence, weights=None, cum_weights=None, k=1)
# No qual:
#
# sequence: é obrigatório e representa a sequência original de elementos, que pode ser uma lista,
# uma tupla ou um conjunto de números;
# weights: é opcional e indica a probabilidade relativa de repetição para cada elemento;
# cum_weights: é opcional e indica a probabilidade acumulada de repetição de cada elemento;
# k: é opcional e indica o número de elementos retornado pela função, sendo o valor padrão igual a 1.

print(max(x) - min(x))
print(x)
