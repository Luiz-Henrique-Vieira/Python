import os
os.system ('cls')

import math

raio = float(input('Digite o raio da circunferencia em centimetros:   '))
c = 2 * math.pi * raio
a= math.pi **raio 
print(f'o comprimento da circunferencia é igual a {c: .2f} cm')
print(f'A area do circulo é igual a {a: .2f} cm²')
