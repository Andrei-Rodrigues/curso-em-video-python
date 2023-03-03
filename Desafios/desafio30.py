'''Crie um programa que leia um número inteiro
e motre na tela se ele é PAR ou Ímpar.'''

'''print('Verifique se o número é par ou ímpar')

print('')

num = int(input('Digite um número: '))

print('')

if num % 2 == 1:
  print('O número é ímpar')
else:
  print('O número é par')'''

#Correção

número = int(input('Me diga um número qualquer: '))
resultado = número % 2

if resultado == 0:
  print('O número {} é PAR'.format(número))
else:
  print('O número {} é IMPAR'.format(número))
