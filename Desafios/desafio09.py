#Faça um programa que leia um número inteiro
#qualquer e mostre na tela a sua tabuada.

#num = int(input('Digite um número para ver a sua tabuada: '))
#v1 = num * 1
#v2 = num * 2
#v3 = num * 3
#v4 = num * 4
#v5 = num * 5
#v6 = num * 6
#v7 = num * 7
#v8 = num * 8
#v9 = num * 9
#v10 = num * 10
#print(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)

#Correção

num = int(input('Digite um número pra ver a sua tabuada: '))
print('-' * 12)
print('{} x {} = {:2}'.format(num, 1, num*1))
print('{} x {} = {:2}'.format(num, 2, num*2))
print('{} x {} = {:2}'.format(num, 3, num*3))
print('{} x {} = {:2}'.format(num, 4, num*4))
print('{} x {} = {:2}'.format(num, 5, num*5))
print('{} x {} = {:2}'.format(num, 6, num*6))
print('{} x {} = {:2}'.format(num, 7, num*7))
print('{} x {} = {:2}'.format(num, 8, num*8))
print('{} x {} = {:2}'.format(num, 9, num*9))
print('{} x {} = {:2}'.format(num, 10, num*10))
print('-' * 12)
