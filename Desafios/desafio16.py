#crie um programa que leia um número real qualquer
#pelo teclado e mostre na tela a sua porção inteira

#Ex:
#Digite um número 6.127
#o número 6.127 tem a
#parte inteira 6.

#import math

#num = float(input('Digite um número decimal para vericar o seu valor inteiro: '))
#int = math.floor(num)
#print('O número {} tem a parte inteira {}'.format(num,int))

#Correção

'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digital foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
