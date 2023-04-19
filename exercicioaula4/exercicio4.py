import os
os.system ('cls')

agua = float(input("Digite o valor da sua conta de agua: "))
energia = float(input('Digite o valor da sua conta de energia: '))
telefone = float(input('Digite o valor da sua conta de telefone:'))
salario = float(input("Digite o seu salário: "))

somacontas = agua + energia + telefone
print(f'Você tem R${somacontas} de dividas.')

if somacontas <= salario:
    print(f'Você tem um salário de R${salario: .2f}, e está quite no serasa, parabéns')
else:
    print('Você não possui salário suficiente para pagar as contas, logo seu nome está no serasa.')