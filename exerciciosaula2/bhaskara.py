import os
os.system('cls')

import math

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

d = b**2 - 4*a*c

x1= (- b + math.sqrt(d)) / (2*a)
x2= (- b - math.sqrt(d)) / (2*a)

print(f"x1={x1:.2F} /n x2={x2:.2f}")