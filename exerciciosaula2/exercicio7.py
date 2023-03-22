import os
os.system('cls')

# solicita ao usuário uma temperatura em Celsius
tc = float(input("Digite a temperatura em Celsius: "))

# converte para Fahrenheit e Kelvin
tf = 1.8 * tc + 32
tk = tc + 273

# exibe as temperaturas convertidas
print("Temperatura em Fahrenheit:", tf)
print("Temperatura em Kelvin:", tk)

