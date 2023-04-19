import os
os.system ('cls')
num = int(input("Digite um numero: "))

result = "par" if num%2 == 0 else "impar"

print(f'O numero {num} é {result}')