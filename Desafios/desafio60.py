#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex:
#5! = 5x4x3x2x1=120

# print('verifique o fatorial do numero')
# num = int(input('Digite um numero: '))
# fatorial = 1
#
# while num > 0:
#     fatorial = num * fatorial
#     num = num - 1
# print('o fatorial é {}'.format(fatorial))

#Correção

#Uma maneira de fazer
# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))