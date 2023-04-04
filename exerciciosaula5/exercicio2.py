import os
os.system('cls')

import math

a = int(input("Digite seu primeiro numero inteiro: "))
b = int(input("Digite um segundo numero inteiro: "))
c = int(input("Digite um terceiro numero inteiro: "))

delta = b*b - 4*a*c

if (delta < 0):
    print('Não existe raizes reais.')
elif (delta == 0):
    x = -b /(2*a)
    print(f'Temos como solução duas raizes iguais ao valor de {x}')

else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (- b - math.sqrt(delta)) / (2*a)
    print("Temos como solução duas raizes diferentes.")
    print(f"X1= {x1}")
    print(f"X2={x2}")