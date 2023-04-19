import os
os.system('cls')

valor_compra = float(input('Digite o valor da compra: '))
desconto = (20 * valor_compra) /100
valor_t = (valor_compra - desconto)


if valor_compra >= 200:
    print(f"Você ganhou um desconto de 20% na sua compra e deu: {valor_t}")
else:
    print(f'Você não recebeu desconto, sua compra deu: {valor_compra}')