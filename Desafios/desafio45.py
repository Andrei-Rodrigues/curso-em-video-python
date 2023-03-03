#Crie um programa que faço o computador jogar Jokenpô com você.

'''import random

print('JOKENPÔ')

print('')

jogo = ['Pedra', 'Papel', 'Tesoura']

computador = random.choice(jogo)

escolha = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).lower()

if computador == 'Pedra' and escolha == 'tesoura':
    print('A escolha da máquina foi {}.'.format(computador))
    print('Que pena, a máquina venceu')

elif computador == 'Tesoura' and escolha == 'pedra':
    print('A escolha da máquina foi {}.'.format(computador))
    print('Parabéns! Você venceu!')

elif computador == 'Tesoura' and escolha == 'papel':
    print('A escolha da máquina foi {}.'.format(computador))
    print('Que pena, a máquina venceu')

elif computador == 'Papel' and escolha == 'tesoura':
    print('A escolha da máquina foi {}.'.format(computador))
    print('Parabéns! Você venceu!')

elif computador == 'Papel' and escolha == 'pedra':
    print('A escolha da máquina foi {}.'.format(computador))
    print('Que pena, a máquina venceu')

elif computador == 'Pedra' and escolha == 'papel':
    print('A escolha da máquina foi {}.'.format(computador))
    print('Parabéns! Você venceu!')

else:
    print('A escolha da máquina foi {}.'.format(computador))
    print('Empate')'''
import time
#Correção

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('')
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
