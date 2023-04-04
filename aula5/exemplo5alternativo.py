import os
os.system('cls')

valor = float(input('Digite o valor da compra: '))
parcelas = int(input('Em quantas parcelas deseja? ' ))

match(parcelas):
    case 2: valor = valor * 1.03

    case 4: valor = valor * 1.07

    case 6: valor = valor * 1.09
    
    case 8: valor = valor * 1.12
        
    case _: valor = -1