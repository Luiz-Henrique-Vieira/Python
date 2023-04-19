import os
os.system('cls')

import math

reais = float(input('Digite o valor em reais do dolar hoje: '))
dolar = float(input('Digite a quantidade de dólares você deseja converter: '))

reais = reais * dolar

print(f'Você teria: {reais: .2f} R$')