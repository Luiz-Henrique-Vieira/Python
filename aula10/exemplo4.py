import os
os.system('cls')
num = []

soma= 0
maior = 0
while True:
    n = int(input('DIgite um numero inteiro(0 sair)'))
    if n == 0: break
    num.append(n)
    soma += n

for n in num:
    if n > maior:
        maior = n

media= soma/len(num)
print(f'A media é {media: .2f}')
print(f'O maior numero é {maior}')
print(num)