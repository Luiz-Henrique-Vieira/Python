import os
os.system('cls')

import math

bmaior = float(input('Digite o lado maior: '))
bmenor = float(input('DIgite o lado menor: '))
h= float(input('Digite a altura do triangulo: '))

volume = h/3*(bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)

print(f'O volume do tronco da piramide é de {volume: .2f}')