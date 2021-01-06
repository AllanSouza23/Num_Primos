def verifica_primos(num):
    #Esta função verifica se há números primos até o número digitado

    #Variáveis de controle
    aux2 = num
    aux3 = 0
    
    if aux2 >= 3:
        #Caso o número digitado seja maior que 3, é impresso os dois primeiros números primos que existem de 0 a 100
        print(2, 3, end=' ')  
    elif aux2 == 2:
        #Caso o número digitado seja igual a 2, é impresso apenas o primeiro número primo que existe de 0 a 100
        print(2)
    else:
        #Caso o número digitado seja menor que 2, não há nenhum número primo entre 0 ao numero digitado
        print('Não há números primos antes do valor digitado.')
    
    while aux3 < num:
        #Enquanto o valor de aux3 for inferior ao valor do número digitado, ainda há números para verificar
        aux = (aux3 ** (0.5))
        aux = int(aux)
        aux1 = 0
        
        while aux >= 2:
            #Enquanto a raiz quadrada do valor digitado for maior ou igual a 2, deve-se verificar se ele é primo
            
            if aux3 % aux == 0:
                #Caso o número dividido por sua raiz tenha resto 0, este número não é primo 
                aux1 += 1
            
            if aux == 2:
                if aux1 == 0:
                    #Caso a variável de controle aux1 for igual a 0, este número não possui divisor inteiro fora 1 e ele mesmo, desta forma ele é impresso
                    print(aux3, end= ' ')
            aux -= 1
        #Acrescenta mais 1 à variável de controle, repetindo até que se chegue ao número digitado
        aux3 += 1 
    
def é_primo(num):
    #Esta função verifica se o número digitado é primo, e retorna ao programa principal "True" ou "False"
    
    #Variáveis de controle
    div = 0
    x = 0

    while x != num:
        #Enquanto a variável de controle "x" for diferente do número digitado, há verificação se ele é divisível por outro número inteiro exceto 1 e ele mesmo.
        
        for x in range(1, num + 1):
            #Para "x" de 1 até o valor digitado, é verificado o resto da divisão.   
            if num % x == 0:
                #Caso o resto da divisão do valor digitado por "x" seja 0, este número é incrementado à variável "div" 
                div +=1         

    if div > 2 and x == num or num <=1:
        #Se o número de divisões com resto 0 supere 2 (ou seja, divisão com resto 0 além de por 1 e por ele mesmo) ou este número digitado seja menor ou igual a 1, temos a certeza que ele não é primo, retornando "False" ao programa principal
        return False

    elif div <= 2 and x == num:
        #Se o número de divisões com resto 0 seja igual a 2 (ou seja, divisão com resto 0 além de por 1 e por ele mesmo) e a variável "x" se igualar ao valor digitado, temos a certeza que ele é primo, retornando "True" ao programa principal
        return True

#Início do programa principal
#Pede para que o usuário insira um número de 0 a 100
numero = int(input('Digite um número de 0 a 100: '))

while numero < 0 or numero > 100:
    #Enquanto o número digitado for ou menor que 0 ou maior que 100, o programa pergunta novamente ao usuário um número entre 0 e 100
    print('O valor digitado não está entre 0 e 100.')
    numero = int(input('Digite um número de 0 a 100: '))

#Atribui à variável "resposta" um valor booleano(lógico), como retorno da função "é_primo(numero)"    
resposta = é_primo(numero)

if resposta == False:
    #Se "resposta" receber o valor "False", é informado ao usuário que o número não é primo
    print(f'\nO número {numero} NÃO é primo!')

else:
    #Caso contrário, o usuário é informado que o número é primo
    print(f'\nO número {numero} É primo!')

#Escreve os números primos de 0 até o número digitado, incluindo ele caso também seja primo, utilizando a função "verifica_primos(numero)"
print(f'Os números primos até {numero} em ordem crescente, o incluindo caso seja primo, são:')
verifica_primos(numero)

if resposta == True and numero > 3:
    #Caso o número também seja primo, ele é incluso no fim da escrita dos demais números primos
    print(numero, end=' ')
print('\n')

#Fim do programa principal
