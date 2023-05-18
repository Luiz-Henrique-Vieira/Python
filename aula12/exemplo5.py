import os
os.system('cls')

imc = lambda peso,altura: peso/altura**2
    
peso= int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

resultado = imc(peso,altura)
print(f'Seu imc é {resultado: .2f} kg/m²')
