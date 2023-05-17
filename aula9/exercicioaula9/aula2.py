import os
os.system('cls')

num = int(input('Digite um numero com três algarismos: '))
inverso = int(str(num)[::-1]) #para inverter os numeros
soma = num + inverso
print(f'O inverso do numero é {inverso}')
print(f'A soma é {num} + {inverso} = {soma}')