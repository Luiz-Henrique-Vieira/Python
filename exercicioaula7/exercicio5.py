import os
os.system('cls')

contagem_masculino = 0
soma_altura_masculino = 0
contagem_feminino = 0
soma_altura_feminino = 0

while True: 
    sexo = input('Digite o sexo do aluno [M/F]: ')
    
    if sexo.upper() not in ['M', 'F']:
        print("Por favor, digite 'M' para masculino ou 'F' para feminino ")
        continue
    altura = float(input('Digite a altura em metros: '))
    
    if sexo.upper() == 'M':
        contagem_masculino += 1
        soma_altura_masculino += altura
    else:
        contagem_feminino += 1
        soma_altura_feminino += altura
    
    continuar = input('Deseja inserir dados de outro aluno? (S/N): ')
    if continuar.upper() != 'S':
        break
    
    
if contagem_masculino > 0:
    media_altura_masculino = soma_altura_masculino / contagem_masculino
    print(f'A media de altura dos alunos masculinos é: {media_altura_masculino: .2f}')
else:
    print('Nenhum aluno masculino registrado')
    
if contagem_feminino > 0: 
    media_altura_feminino = soma_altura_feminino / contagem_feminino
    print(f"A media de altura das alunas femininas é de {media_altura_feminino: .2f}")
else:
    print('Nenhuma aluna feminina registrada')