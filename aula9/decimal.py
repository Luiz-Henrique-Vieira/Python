decimal = int(input('Digite um numero decimal: '))
print('[2]Binário\n[8]Octal\n[16]Hexadecimal')
base = int(input('Escolha uma base para conversão: '))

num_conv =''
digitos = '0123456789ABCDEF'
while decimal > 0:
    num_conv = (digitos[decimal % base]) + num_conv
    decimal = decimal // base

print(f'O numero convertido para a base {base} é igual a {num_conv}')