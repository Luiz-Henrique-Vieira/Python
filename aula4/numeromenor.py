import os
os.system('cls')

a = int(input('digite o numero A:'))
b = int(input('digite o numero B:'))
c = int(input('digite o numero C:'))

if a > b and b < c:
    print('O menor valor é o B')
else:
    print('O menor numero não é o B')
