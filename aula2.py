aluno = str(input('Nome do aluno: '))

a = float(input('Primeiro bimestre: '))
if a >= 10:
    print('Nota invalida, por favor digite um nota até 10.')
    a = float(input('Primeiro bimestre: '))

b = float(input('Segundo bimestre: '))
if b >= 10:
    print('Nota invalida, por favor digite um nota até 10.')
    b = float(input('Segundo bimestre: '))

c = float(input('Terceiro bimestre: '))
if c >= 10:
    print('Nota invalida, por favor digite um nota até 10.')
    c = float(input('Terceiro bimestre: '))

d = float(input('Quarto bimestre: '))
if d >= 10:
    print('Nota invalida, por favor digite um nota até 10.')
    d = float(input('Quarto bimestre: '))

media = (a + b + c + d) / 4

print(f'O aluno {aluno} ficou com a media de {media}')
