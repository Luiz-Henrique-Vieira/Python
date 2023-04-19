import os
os.system('cls')

binario = input("Digite um numero binario: ")
n = len(binario)-1
decimal = 0

for d in binario:
    decimal = decimal + int(d)*2**n
    n = n - 1

print(decimal)