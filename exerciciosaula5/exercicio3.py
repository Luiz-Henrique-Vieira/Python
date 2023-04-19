import os
os.system('cls')

produto = input('Digite o nome do produto: ')
valor_compra = float(input('Digite o valor da compra: '))

if valor_compra < 10.00:
    valor_venda = valor_compra * 70/(100)
    print(f'Você vendeu:{produto} e lucrou R$:{valor_venda}')

elif valor_compra < 30.00:
    valor_venda = valor_compra * 50/(100)
    print(f'Você vendeu:{produto} e lucrou R$:{valor_venda}')

elif valor_compra < 50.00:
    valor_venda = valor_compra * 40/(100)
    print(f'Você vendeu:{produto} e lucrou R$:{valor_venda}')

else:
    valor_venda = valor_compra * 30/(100)
    print(f'Você vendeu:{produto} e lucrou R$:{valor_venda}')