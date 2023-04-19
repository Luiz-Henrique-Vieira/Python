import os
os.system('cls')

num = int(input("Tente a sorte e digite um numero: "))

result = "correto, parabéns" if num == 7 else "incorreto" 

print (f"O numero {num} está {result}")