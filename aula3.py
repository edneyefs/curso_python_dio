n = int(input('Digite um número: '))

div = 0
for i in range(1, n+1):
    resto = n % i
    print(i, resto)
    if resto == 0:
        div += 1
if div == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
