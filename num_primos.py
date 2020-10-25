num = int(input('Digite um numero: '))
aux = 0
aux1 = 0
aux2 = num

while num > 1:
    aux = (num ** (1/2))
    aux = int(aux)
    aux1 = 0
    while aux >= 2:
        if num % aux == 0:
            aux1 += 1
        if aux == 2:
            if aux1 == 0:
                print(num, end= ' ')
        aux -= 1
    num -=1
if aux2 >= 3:
    print(3, 2)   