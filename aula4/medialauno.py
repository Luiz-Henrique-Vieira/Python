import os
os.system('cls')

n1= float(input('Digite a primeira nota: '))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2)/2

if m >= 6:
    print(f'Você tirou {m} e foi aprovado, parabéns.')
else:
    print(f"Você tirou {m} e foi reprovado, boa sorte na proxima vez.")