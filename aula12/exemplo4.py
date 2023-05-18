import os
os.system('cls')
def soma(a,b):
    return a+b

while True:
    n1 = int(input('Qual o 1° numero? '))
    n2 = int(input('Qual o 2° numero? '))

    print(soma(n1,n2))
    if(input('Deseja Continuar?')) in 'nN': break