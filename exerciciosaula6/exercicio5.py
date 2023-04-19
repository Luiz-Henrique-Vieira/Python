import os
os.system('cls')

import math

metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros_tinta = metros_quadrados / 3
latas_tinta = math.ceil(litros_tinta / 18)
preco_total = latas_tinta * 80

print(f"Você precisará de {latas_tinta} latas de tinta para pintar a área.")
print(f"O preço total da compra será de R$ {preco_total} reais.")