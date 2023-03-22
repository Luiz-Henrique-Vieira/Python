import os
os.system('cls')

satual= float (input('Digite seu salario atual: '))
snovo = satual + (satual * (5/100))


print(f'Seu salario novo é: {snovo:.2f}')
print(f"Sua comissão foi de: {satual * 5/100: .2f}")
