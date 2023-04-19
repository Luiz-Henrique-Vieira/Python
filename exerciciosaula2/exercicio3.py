import os
os.system('cls')
import math

distancia = float(input('Digite a distancia entre as cidades em km: '))
tempo = float(input('Digite o tempo percorrido entre as cidades: '))

velocidade= distancia / tempo 

print(f'A velocidade media foi de  {velocidade:.2f} km/h')