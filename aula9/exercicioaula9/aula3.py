import os
os.system('cls')

string = input("Entre em uma string: ")
stringAlta = string.upper()

caractere = set(stringAlta)

for caracteres in caractere:
    aparece = stringAlta.count(caracteres)
    print(f'O caractere {caracteres} aparece {aparece} vezes')