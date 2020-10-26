def verifica_primos(num):
    aux = 0
    aux1 = 0
    aux2 = num
    aux3 = 0
    while aux3 == 0:
        while num > 1:
            aux = (num ** (0.5))
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
            aux3 = 1
        elif aux2 == 2:
            print(2)
            aux3 = 1
        else:
            print('Não há números primos antes do valor digitado.')
            aux3 = 1

def é_primo(num):
    a = num
    div = 0
    while a != 0:
        for x in range(1, num + 1):
            if num % a == 0:
                div +=1
                a -=1
            else:
                a -=1
    if div >2 and a == 0 or num <=1:
        return False
    elif div < 3 and a ==0:
        return True

numero = int(input('Digite um número de 0 a 100: '))
if numero < 0 or numero > 100:
    print('O valor digitado não está entre 0 e 100.')
    numero = int(input('Digite um número de 0 a 100: '))
print(f'Os números primos até {numero}, incluindo ele são:')
verifica_primos(numero)
resposta = é_primo(numero)
if resposta == False:
    print(f'\nO número {numero} NÃO é primo!')
elif resposta == True:
    print(f'\nO número {numero} É primo!')
