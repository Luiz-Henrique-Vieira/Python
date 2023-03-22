import os
os.system("cls")

nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
meses = idade * 12
print(nome)
print(idade)
print(f"{nome} você tem {meses} meses idade")