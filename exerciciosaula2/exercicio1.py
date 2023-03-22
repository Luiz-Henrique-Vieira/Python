import os 
os.system("cls")

altura = float (input('Digite a altura do seu retangulo: '))
base = float (input('Digite a base do seu retangulo: '))

a= (base * altura)
print(f'A area do seu retangulo é: {a:.2f} ')

p = (base + altura) *2
print(f'O perimetro do seu retagunlo é: {p:.2f}')

