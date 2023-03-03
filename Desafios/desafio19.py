#Um professor quer sortear um dos seus quatro alunos
#para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome dele e escrevendo o nome do escolhido.

'''import random

print('Sorteio para verificar quem vai apagar o quadro')

print('')

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno2, aluno3, aluno4]

sorteio = random.choice(alunos)

print('')

print('O aluno sorteado para apagar o quadro foi: {}'.format(sorteio))'''

#Correção

from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))