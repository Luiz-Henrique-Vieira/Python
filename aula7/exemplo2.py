import os
os.system('cls')

soma = 0

for i in range(3):
    num = float(input(f"Digite o {i+1} numero: "))
    #soma = soma + num
    soma += num

print(f'A soma dos numeros é {soma}')

# soma = 0
# num = 2  -> soma = 0 + 2 = 2
