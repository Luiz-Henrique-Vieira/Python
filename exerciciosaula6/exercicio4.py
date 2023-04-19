import os
os.system('cls')

alt= float(input('Digite a sua altura em metros: '))
sex = input('Digite o seu sexo: M | F :')

masc= (72.7*alt) -58
fem = (62.1*alt) -44.7

if sex in "mM":
    print(f'Seu peso ideal é:{masc:.1f}')
elif sex in "fF":
    print(f'Sei peso ideal é: {fem: .1f}')
else:
    print('Aconteceu algo de errado, tente novamente')