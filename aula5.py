conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

#união de conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print(f'União: {conjunto_uniao}')

#intersecção de conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Intersecção: {conjunto_interseccao}')

#diferença de conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print(f'Difereça entre 1 e 2: {conjunto_diferenca}')
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(f'Diferença entre 2 e 1: {conjunto_diferenca2}')

#diferença simetrica "só tem em a ou em b"
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(f'Diferença simétrica: {conjunto_dif_simetrica}')

#pertinencias retornará bool
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_subsetb = conjunto_b.issubset(conjunto_a)
conjunto_superset = conjunto_a.issuperset(conjunto_b)
conjunto_supersetb = conjunto_b.issuperset(conjunto_a)
print(f'Conjunto A: {conjunto_a}')
print(f'Conjunto B: {conjunto_b}')
print(f'Conjunto A é subconjunto de B: {conjunto_subset}')
print(f'Conjunto B é subconjunto de A: {conjunto_subsetb}')
print(f'Conjunto A é um superset de B: {conjunto_superset}')
print(f'Conjunto B é um superset de A: {conjunto_supersetb}')

#removendo duplicidades em list
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

#adiciona elemento
#conjunto.add(5)

#exclui elementos
#conjunto.discard(2)

#print(type(conjunto))
