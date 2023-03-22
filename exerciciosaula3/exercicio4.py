import os
os.system('cls')

vp = float(input('Digite o valor da prestação: '))
multa = float(input('Digite a porcentagem da multa: '))
qntdias = int(input('Digite a quantidade de dias atrasado: '))

prestacao = vp+(vp*(multa/100)*qntdias)

print(f'O valor atualizado da prestação é: {prestacao: .2f}')