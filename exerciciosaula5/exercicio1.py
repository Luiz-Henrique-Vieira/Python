import os
os.system('cls')

idade = int(input('Digite sua idade: ' ))


if idade < 16:
    print('Você ainda é um não-eleitor.')
elif idade  >=18 and idade <= 65:
    print('Eleitor obrigatório!!')
else: 
    print('Você é um eleitor facultativo e não é obrigado a votar.')
