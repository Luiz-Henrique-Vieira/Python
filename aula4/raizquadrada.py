import os
os.system("cls")

import math

num = float(input('Digite um numero inteiro:'))

if num >= 0:

    raiz = math.sqrt(num)
    print(f'A raiz de {num} é {raiz: .2f}')
else:
    print('Não há raiz de numero negativo')

