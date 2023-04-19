import os
os.system('cls')

seg = float(input('Digite a quantidade de segundos para converter: '))
h = seg // 3600
min = seg % 3600 // 60
segundos = seg % 60

print(f'{h: .0f} horas(s), {min: .0f} minutos (s), {segundos: .0f} segundos(s)')