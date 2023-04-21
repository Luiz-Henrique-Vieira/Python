import os
os.system('cls')

naopodevotar = 0
podevotar = 0



for i in range(10):
    idade = int(input(f'Digite a idade {i+1} do aluno: '))
    naopodevotar += idade
    if idade >= 16:
     podevotar += 1    
        
media = naopodevotar/10  
print(f'Alunos que pode votar: {podevotar}')
print(f'A media de alunos que não pode votar é de {media}')

