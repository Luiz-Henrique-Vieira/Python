import os
os.system('cls')

print("Pousada do Paulin")
print("[s] Quarto Simples")
print("[d] Quarto Duplo")
print("[t] Quarto Triplo")

opcao = input('Digite o quarto desejado: ')
if opcao in "sSdDtt":
    diaria = int(input('Quantas diárias? '))

if opcao in 'sS':
    print(f'Total a pagar R${diaria * 255.5}')
elif opcao in "dD":
    print(f'Total a pagar R$ {diaria * 305.5}')
elif opcao in "tT":
    print(f"Total a pagar R${diaria * 355.5}")
else:
    print('Opção de hospedagem inválida')