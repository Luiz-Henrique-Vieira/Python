import os
os.system('cls')

palavra = input('Entre com uma palavra: ')

if palavra == palavra [::-1]:
    print(f'{palavra} é um palíndromo.')
else:
    print(f'{palavra} não é um palíndromo.')
    