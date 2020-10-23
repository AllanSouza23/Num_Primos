# Elabore um programa em Python que recebe um número inteiro positivo qualquer de 0 a 100. O programa deverá verificar e exibir todos os números primos até o valor digitado. 
# A verificação se um número é primo deverá ser implementada por uma função que retorna um valor lógico ("True" ou "False") ao programa (ou script) principal.

def verifica_primo(numero):
    aux = 0
    primos = []
    for x in range (1, numero + 1):
        if numero % x == 0:
            print('\033[0;33;44m', x, end=' ')
            aux += 1
            primos.append(x)
        else:
            print(x, end=' ')
        
    print(f'\nO número {numero} foi divisível {aux} vezes')
    if aux <= 2:
        print(f'O número {numero} é primo!')
    else: 
        print(f'O número {numero} NÃO é primo!') 
    print(primos)
numero = int(input('Digite um número inteiro qualquer de 0 a 100:  '))
verifica_primo(numero)
