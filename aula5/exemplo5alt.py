import os
os.system('cls')

valor = float(input('Digite o valor da compra: '))
parcelas = int(input('Em quantas parcelas deseja? ' ))

if parcelas == 2:   #valor = valor + valor * 3/100
    valor = valor * 1.03
elif parcelas == 4:
    valor = valor * 1.07
elif parcelas == 6:
    valor = valor * 1.09
elif parcelas == 8:
    valor = valor * 1.12
else:
    valor = -1

if valor < 0:
    print('Parcelamento inválido!')
else:
    print(f'Valor da parcela = R${valor/parcelas}')
