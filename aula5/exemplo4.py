import os
os.system('cls')

altura = float(input('Digite sua altura: '))
peso = int(input("Digite seu peso: "))
imc = peso / (altura * altura)
print(f"Seu imc: {imc}")

if imc < 20:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30: 
     print("Você está sobrepeso")
elif imc < 40: 
     print("Você está obeso")
else: 
     print("Você está em obesidade morbida")