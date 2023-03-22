import os
os.system('cls')

gastototal = float(input('Qual foi o valor gasto pelo cliente? : '))
gorjeta = float
gorjeta = gastototal * 10/100
gastototal + gorjeta
gorjeta = gastototal + gorjeta


print(f"O valor gasto total do cliente é de: {gastototal} R$")
print(f'E com o acrescento da gorjeta de 10% o valor total da conta fica: {gorjeta: .2f}')