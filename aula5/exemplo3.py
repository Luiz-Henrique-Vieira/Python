import os
os.system('cls')

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('Numero 1 é o maior') 
elif n2 > n1 and n2 > n3:
    print('Numero 2 é o maior') 
elif n3 > n1 and n3 > n2:
    print('Numero 3 é o maior') 
else:
    print('Os números são iguais.')
