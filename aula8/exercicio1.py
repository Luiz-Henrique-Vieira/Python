import os
os.system('cls')

carneirinho = 0

while True:
    jadormi = input('Eu ja dormi [S/N]?')
    if jadormi in "Ss":
        carneirinho = carneirinho + 1
        print(f'Contei {carneirinho}')
        continue
    elif jadormi in "nN":
        break


