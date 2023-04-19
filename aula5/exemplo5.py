import os
os.system('cls')

valor = float(input('Digite o valor da compra: '))
parcelas = float(input('Em quantas parcelas deseja? ' ))
valor_juros = valor / parcelas 
if parcelas == 2:
    print(f'Valor da parcela R${ valor_juros + (valor * 3)/100}')
elif parcelas == 4:
    print(f'Valor da parcela R$ {valor_juros + (valor * 7)/100}')
elif parcelas == 6:
    print(f"Valor da parcela R${valor_juros + (valor * 9)/100}")
elif parcelas == 8:
    print(f"Valor da parcela: R${valor_juros + (valor * 12)/100}")
else:
    print('Valor de parcelas não indicado')
