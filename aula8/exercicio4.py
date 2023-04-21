import os
os.system('cls')

conta = input('Digite a conta: ')

soma= 0

for n in conta:
    soma += int(n)


    dig = soma % 10
print(f'00{conta}-{dig}')
