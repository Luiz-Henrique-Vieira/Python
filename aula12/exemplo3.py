import os
os.system('cls')

def exibir(num, msg):
    print(f'A mensagem é: {msg}')
    print(f'O numero é: {num}')

msg = input('Digite uma mensagem: ')
num = int(input('Digite um numero: '))

exibir(num, msg)

exibir(3,'😍😍😍😍')