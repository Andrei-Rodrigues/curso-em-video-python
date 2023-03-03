'''Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
último = Souza'''

'''nome = str(input('Digite o seu nome completo: '))

primeiro_segundo = nome.split()
print('O primeiro nome é {}'.format(primeiro_segundo[0]))
print('O segundo nome é {}'.format(primeiro_segundo[1]))'''

#Correção

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
