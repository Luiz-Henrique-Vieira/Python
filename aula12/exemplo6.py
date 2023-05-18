import trigonometria, os #chamando import para importar meu metodo de outro arquivo
os.system('cls')
 

catO = float(input('Qual o cateto oposto? '))
catA = float(input('Qual o cateto adjacente? '))

print(f'Seno = {trigonometria.seno(catO,catA)}')
print(f'cosseno = {trigonometria.cosseno(catO,catA)}')
print(f'tangete = {trigonometria.tangente(catO,catA): .2f}')
