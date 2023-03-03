#O mesmo professor do desafio anterior quer sortear
#a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.

'''import random

print('Sorteio para verificar a ordem de apresentação de trabalhos')

print('')

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print('')

print('A ordem de apresentação dos trabalhos é {}'.format(alunos))'''

#Correção

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
