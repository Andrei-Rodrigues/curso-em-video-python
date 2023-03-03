#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:

#1 para binário
#2 para octal
#3 para hexadecimal

'''import math

num = int(input('Digite um número: '))
bin = bin(num)
oct = oct(num)
hex = hex(num)
print('Escolha a base de conversão')

print('')

print('Digite 1 - Para binário')
print('Digite 2 - Para octal')
print('Digite 3 - Para hexadecimal')

print('')

base_conversao = int(input('Base de conversão: '))

if base_conversao == 1:
    print('O número {} em binário é {}'.format(num, bin))
elif base_conversao == 2:
    print('O número {} em octal é {}'.format(num, oct))
elif base_conversao == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex))'''

#Correção

num = int(input('Digite um número inteiro: '))
print('''Escolha aum das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')