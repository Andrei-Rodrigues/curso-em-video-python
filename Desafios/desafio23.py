'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digítos separados.

Ex:
Digite um número: 1834

Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1'''

'''num = input(('Digite um número: '))

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print('A unidade é {}'.format(unidade))
print('A dezena é {}'.format(dezena))
print('A centena é {}'.format(centena))
print('O milhar é {}'.format(milhar))'''

#Correção


#Primeira maneira de se fazer - trabalhando com string

'''num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(n[3]))
print('Dezena {}'.format(n[2]))
print('Centena {}'.format(n[1]))
print('Milhar {}'.format(n[0]))'''

#Maneira ideal de fazer

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))


