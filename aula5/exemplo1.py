import os
os.system('CLS')

freq= float(input('Qual a frequência do aluno? '))
nota = float(input('Qual a media do aluno? '))

if freq < 75:
    print('reprovado por falta!')
elif nota < 6:
    print('Reprovado por nota!')
else:
    print('aprovado')
