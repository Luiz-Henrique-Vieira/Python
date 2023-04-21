import os
os.system('cls')

arquivo = float(input("Digite o tamanho do arquivo(MB): "))
velocidade = float(input('Digite a velocidade de download (MBPS): '))

tempo = arquivo * 8 / velocidade
min = tempo // 60
segundos = tempo % 60

print(f'Tempo aproximado de download: {min: .0f} minutos e {segundos: .0f} segundos')


