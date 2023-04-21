import os
os.system('cls')
import math

turmas = int(input('Digite a quantidade de turmas: '))
alunos = 0

for i in range(turmas):
    qntdalunos = int(input(f'Digite a quantidade de alunos da turma {i+1}: '))
    alunos += qntdalunos

mediaAlunos = math.ceil(alunos / turmas)

print(f'O numero médio de alunos por turma é {mediaAlunos: .0f}')