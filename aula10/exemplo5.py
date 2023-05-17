import os
os.system('cls')

nomes = []
notas = []

n= int(input('Qual a quantidade de alunos? '))
for i in range(n):
    nome = input('Qual o nome do aluno? ')
    n1= float(input(f'Digite a 1° nota do {nome}:'))
    n2= float(input(f'Digite a 2° nota do {nome}:'))
    media = (n1 + n2)/2
    notas.append(media)
    nomes.append(nome)

print(30*'-')
for i, e in enumerate(nomes):
    print(f'[{i}]- {e}')
print(30*'-')
nome = input('Qual o nome do aluno? ')
i = nomes.index(nome)
resultado = 'APROVADO' if notas[i] > 6 else 'REPROVADO'
print (f'O aluno {nomes[i]} foi {resultado}')
print(f'Media: {notas[i]:.2f}')