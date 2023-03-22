import os
os.system('cls')

import math

angulograus = float(input('Digite o valor do angulo: '))

angulorad = math.radians(angulograus)

seno = math.sin(angulograus)
cos = math.cos(angulograus)
tan = math.tan(angulograus)


print(f'O seno de angulo é: {seno}')
print(f'O cosseno de angulo é: {cos}')
print(f'A tangente de angulo é: {tan}')