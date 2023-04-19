import os
os.system('cls')

menos= 0
contador = 0
valor_menor = None

while True:
    num = float(input('Digite um numero real(ou digite 0 para sair): '))
    if num == 0:
        break
    if num > 0:
        contador += 1
    elif num < 0:
        menos += 1
    
    
    if valor_menor is None or num < valor_menor:
        valor_menor = num
        
print(f'Você tem {contador} numeros positivos')    
print(f'Você tem {menos} numeros negativos')
print(f'O menor valor entre eles é{valor_menor}')
        
        

    