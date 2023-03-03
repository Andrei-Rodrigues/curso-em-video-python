'''Crie um programa que leia o nome completo de uma pessoa e mostre:

.O nome com todas as letras maiúsculas.

.O nome com todas minúsculas.

.Quantas letras ao todo (sem considerar espaços).

.Quantas letras tem o primeiro nome.'''

'''nome = str(input('Digite o seu nome: '))

maiscula = nome.upper()
print(maiscula)

minuscula = nome.lower()
print(minuscula)

qtd_letras = len(nome.replace(' ', ''))
print(qtd_letras)

separar = nome.split()[0]
print(len(separar))'''

#Correção

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em maiúsculas é {}'.format(nome.lower()))
#Subtração
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#Quantidade do primeiro espaço
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
