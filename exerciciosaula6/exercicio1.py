import os
os.system('cls')

satual= float (input('Digite seu salario atual: '))
total_vendas= int(input('Digite o total de vendas:'))
s_final = satual + (total_vendas * (4/100))


print(f"Sua comissão foi de: {total_vendas * 4/100: .2f}")
print(f' Salario final: {s_final:.2f}')