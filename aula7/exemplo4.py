import os
os.system('cls')

cont= 0

while cont < 10:
    nome = input('Qual o nome do aluno? ')
    n1= float(input(f'Qual a primeira nota do {nome}? '))
    n2= float(input(f'Qual a segunda nota do {nome}? '))
    media = (n1 + n2)/2
    print(f"A media do aluno {nome} é {media: .2f}")

    cont = cont + 1