def verifica_primos(num):
    aux2 = num
    aux3=0
    if aux2 >= 3:
        print(2, 3, end=' ')  
    elif aux2 == 2:
        print(2)
    else:
        print('Não há números primos antes do valor digitado.')
    while aux3 < num:
        aux = (aux3 ** (0.5))
        aux = int(aux)
        aux1 = 0
        
        while aux >= 2:
            if aux3 % aux == 0:
                aux1 += 1
            if aux == 2:
                if aux1 == 0:
                    print(aux3, end= ' ')
            aux -= 1
        aux3 +=1 
    

def é_primo(num):
    div = 0
    x=0
    while x != num:
        for x in range(1, num + 1):
            if num % x == 0:
                div +=1         
    if div >2 and x == num or num <=1:
        return False
    elif div < 3 and x == num:
        return True

numero = int(input('Digite um número de 0 a 100: '))
while numero < 0 or numero > 100:
    print('O valor digitado não está entre 0 e 100.')
    numero = int(input('Digite um número de 0 a 100: '))
resposta = é_primo(numero)
if resposta == False:
    print(f'\nO número {numero} NÃO é primo!')
else:
    print(f'\nO número {numero} É primo!')
print(f'Os números primos até {numero} em ordem crescente, o incluindo caso seja primo, são:')
verifica_primos(numero)
if resposta == True and numero > 3:
    print(numero, end=' ')
print('\n')
