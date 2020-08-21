# a = 0
# while a <= 10:
#     print(a)
#     a += 1

aluno = str(input('Nome do aluno: '))

a = float(input('Primeiro bimestre: '))
while a > 10:
    a = float(input('Nota invalida, por favor digite um nota até 10. Primeiro bimestre: '))

b = float(input('Segundo bimestre: '))
while b > 10:
    b = float(input('Nota invalida, por favor digite um nota até 10. Segundo bimestre: '))

c = float(input('Terceiro bimestre: '))
while c > 10:
    c = float(input('Nota invalida, por favor digite um nota até 10. Terceiro bimestre: '))

d = float(input('Quarto bimestre: '))
while d > 10:
    d = float(input('Nota invalida, por favor digite um nota até 10. Quarto bimestre: '))

media = (a + b + c + d) / 4

print(f'O aluno {aluno} ficou com a media de {media}')
