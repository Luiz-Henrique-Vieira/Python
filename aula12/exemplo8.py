import os
os.system('cls')
soma = lambda a,b: a+b
sub = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda a,b: a/b


menu = ['Soma','Subtação','Multiplicação','Divisão','Sair',]

while True:
    os.system('cls')
    print('Calculadora lambda')
    for n, item in enumerate(menu):
        print(f'[{n+1}]- {item}')


    op = int(input('Digite uma opção: '))
    if op == 5: break
    elif str(op) not in '1234': print('Opção inválida!')
    else:
        n1= float(input('Digite o 1° numero:'))
        n2 = float(input('Digite o 2° numero:'))
        if op == 1: print(f'{n1} + {n2} = {soma(n1,n2)}')
        elif op == 2: print(f'{n1} - {n2} = {sub(n1,n2)}')
        elif op == 3: print(f'{n1} * {n2} = {mult(n1,n2)}')
        else: print(f'{n1} / {n2} = {div(n1,n2)}')
    input('\nEnter continua...')
os.system('cls')
print('Obrigado por utilizar nosso serviços')
print('Volte sempre')