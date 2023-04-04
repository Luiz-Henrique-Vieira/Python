import os
os.system('cls')

num1= float(input('Digite o primeiro numero:'))
num2= float(input('Digite o segundo numero:'))
calcule = input('Digite o sinal que você deseja calcular: ')

if calcule in "+":
    print(f'Resultado da sua conta foi: {num1 + num2}')
elif calcule in "-":
    print(f'Resultado da sua conta foi: {num1 - num2}')
elif calcule in "*":
    print(f'Resultado da sua conta foi: {num1 * num2}')
elif calcule in "/":
    print(f'Resultado da sua conta foi: {num1 / num2}')
else:
    print('Digite uma operação matemática e tente novamente...')
