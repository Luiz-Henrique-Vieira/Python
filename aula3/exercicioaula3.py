import os
os.system('cls')

import math

num= int(input('Digite um numero com tres digitos: '))
d1= num // 100
d2 = num % 100 // 10    #2*100 + 3*10 * 4 #
d3 = num % 10
inverso = d3*100 + d2*10 + d1
print('O inverso do numeo digitado é: ', inverso)    