#Faça um programa que leia o comprimento
#do cateto oposto e do cateto adjacente
#de um triângulo retângulo, calcule e mostre
#o comprimento da hipotenusa.

import math

print('Verifique a hipotenusa de um triângulo retângulo')

print('')

cat_op = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))
calc = (cat_op ** 2) + (cat_adj ** 2)
hip = math.sqrt(calc)

print('')

print('A hipotenusa do triângulo retângulo é {}'.format(hip))

#Correção

'''co = float(input('Comprimento oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

'''from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
