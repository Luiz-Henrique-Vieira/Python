import os
os.system('cls')

x = float(input("Digite a coordenada x do ponto P: "))
y = float(input("Digite a coordenada y do ponto P: "))

if x > 0 and y > 0:
    print(f"O ponto P({x}, {y}) está no primeiro quadrante")
elif x < 0 and y > 0:
    print(f"O ponto P ({x}, {y}) está no segundo quadrante")
elif x < 0 and y < 0:
    print(f"O ponto P ({x}, {y}) está no terceiro quadrante")
elif x > 0 and y < 0:
    print(f"O ponto P ({x}, {y}) está no quarto quadrante")
else:
    print(f"O ponto P ({x}, {y}) está sobre um dos eixos.")

