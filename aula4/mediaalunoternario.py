import os
os.system('cls')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

m = (n1 + n2)/2

result = "você foi aprovado" if m >=6.0 else "você não foi aprovado"
print(f"Sua nota foi {m} e {result}")