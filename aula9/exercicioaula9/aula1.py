import os
os.system('cls')

email = input('Digite seu email: ')
arroba = email.rfind('@')
dominio = email[arroba + 1:]

print(f'O dominio do seu email é {dominio}')
