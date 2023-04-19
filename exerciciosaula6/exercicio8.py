import os
os.system('cls')

nome = input('Digite seu nome: ')
h = float(input('Que horas são? '))

if h > 5 and h <= 12:
    print(f"Bom dia {nome}")
elif h >= 13 and h <=18:
    print(f'Boa tarde {nome}')
else:
    print(f'Boa noite, {nome}')