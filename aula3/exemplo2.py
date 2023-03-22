import os
os.system('cls')

import math

num = float(input('Digite um numero real: '))
absoluto = math.fabs(num)
inteiro = math.trunc(absoluto)
raiz = math.sqrt (absoluto)
fatorial = math.factorial(inteiro)

print(f'Absoluto: {absoluto}')
print(f'inteiro: {inteiro}')
print(f'raiz: {raiz: .2f}')
print(f'Fatorial: {fatorial}')

