import os
os.system("cls")

import math


a = int(input('digite o valor de A:'))
b = int(input('digite o valor de B:'))
c = int(input('digite o valor de C:'))

print('****************************************')


delta = b*b - 4*a*c

if (delta<0):
    print('não tem raizes reais')
elif(delta ==0): 
    x = -b /(2*a)
    print('temos como solução duas raizs iguais ao valor de' , x)
    
else:
    x1= (-b + math.sqrt(delta)) / (2*a)
    x2= (- b - math.sqrt(delta)) /(2*a)
    print('temos como solução duas raizese difrentes')
    print('x1=',x1)
    print('x2=',x2)