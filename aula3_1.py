a = int(input('Entre com um valor: '))
for num in range(a+1):
    div = 0
    for i in range(1, num+1):
        resto = num % i
        #print(i, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)
