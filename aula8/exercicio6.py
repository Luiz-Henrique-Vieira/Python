import os
os.system('cls')

hora_aula = float(input('Digite o valor da hora aula: '))
carga = float(input('Digite a carga horária semanal: '))

salario_base = hora_aula* carga * 4.5
adicional = salario_base * 1/6
salario_final = salario_base + adicional

print(f'o salario final é : R$ {salario_final: .2f}')