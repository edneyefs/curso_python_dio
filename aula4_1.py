#tuplas são imutáveis, ou seja, não consigo modificar um de seus itens.
tupla = (1, 10, 12, 14)
print(tupla)
print(tupla[2])

#quantos elementos tem na tupla
print(len(tupla))

#transforma a tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)