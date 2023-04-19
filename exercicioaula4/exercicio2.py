import os
os.system('cls')

t = input ('Digite o seu turno de trabalho (N para noturno ou D para diurno): ')
h = float(input('Digite a quantidade de horas trabalhadas: '))

if t == "N":
    valor_hora = 45.0
else:
    valor_hora = 37.5

s = valor_hora * h

print(f'O valor do seu sálario é R$ {s:.2f}')



