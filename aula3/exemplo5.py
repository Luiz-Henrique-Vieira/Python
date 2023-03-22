import os
os.system('cls')

import math

sombra= float(input('Digite o comprimento da sombra em m: '))
angulo = math.radians(float(input('Digite o angulo em graus: ')))
altura = math.tan (angulo) * sombra

print(f'A altura do predio é de {altura: .2f} m')