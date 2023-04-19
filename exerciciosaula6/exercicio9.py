import os
os.system('cls')

import math

print("Entrada: ")

num1 = float(input('Digite o primero numero: '))
num2 = float(input('Digite o segundo numero: '))
print('[1] Media')
print('[2] Diferença maior-menor')
print('[3] Produto')
print('[4]  Divisão n1/n2')
what = input('O que você deseja saber? ')


if what in "1":
    print(f'A media dos numeros é {(num1 * num2) / 2} ')
elif what in "2":
    if num1 > num2:
        res = num1 - num2
        print(f'A diferença entre os numeros é de {res}')
    else:
        res = num2 - num1
        print(f'A diferença entre os numeros é de {res}')
elif what in "3":
    print(f'Produto: {num1 * num2: .1f}')
elif what in "4":
    if num2 == 0:
       print('O numero não pode ser dividido por 0')     
    else:
        print(f'O resultado dessa divisão é {num1 / num2}')
else:
    print('Opção inválida')