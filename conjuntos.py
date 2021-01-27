# conjuntos aritimeticos em python
#
# conjunto = {1, 2, 3, 4, 4, 2}
# print(conjunto)
# conjunto.add(11) #adiciona elemento
# print(conjunto)
# conjunto.discard(3)  # remove
# print(conjunto)

"""
uniao de conjunto
"""
conjunto = {1, 2, 3, 4, 5, 6}
conjunto2 = {6, 7, 8, 9, 10}
conjunto_uniao = conjunto.union(conjunto2)  # resultado dos dois numeros
print('Uniao: {} ' .format(conjunto_uniao))
conjunto_intersecao = conjunto.intersection(conjunto2) # mesmo numero nos dois conj.
print('Intersecao: {} ' .format(conjunto_intersecao))
conjunto_diferenca = conjunto.difference(conjunto2) # numero diferentes noi sdois conj.
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença: {} ' .format(conjunto_diferenca))
print('Uniao: {} ' .format(conjunto_diferenca2))
conjunto_dif_simetrico = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica: {} ' .format(conjunto_dif_simetrico))
conjunto_a = {1, 2, 3} # retorna se o conjunto é um subconjunto de outro conjunto
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

lista = ['gato', 'cachorro', 'elefante', 'gato']
print(lista)
conjunto_animais = set(lista) #transforma lista em conjunto e retira a duplicidade
print(conjunto_animais)

lista_animais = list(conjunto_animais) #tranforma conjutos em lista
print(lista_animais)


mariana = 2  # dona da casa
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3

dedos = {mariana, renato, larissa, rafael, augusto, rafaela}

participantes = \
    ______ #quantidade de participantes

somaDedos = ______ #soma dos valores de cada dedo

dedoapontadopara = 0

for x in range(somaDedos):

  if dedoapontadopara > participantes:

     dedoapontadopara = 0

  dedoapontadopara += 1

dedos = _______ #converter dedos para arquivo tipo 'list'

print('No final o dedo foi apontado para {}.'.format(dedos[dedoapontadopara]))


