import os
os.system('cls')



a = int(input('Digite sua idade em anos: '))
m = int(input('Digite a sua idade em meses: '))
d= int(input('Digite a sua idade em dias: '))

dias= a*365 + m*30 + d

print(f'A sua idade em dias é: {dias}')
