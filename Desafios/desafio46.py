#Faça um programa que mostre na tela uma contagem
#regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

'''from time import sleep
import emoji

for tempo in range(10, -1, -1):
    sleep(1)
    print(tempo)
    sleep(0.5)
print('BUUUUMMM', end='')
print(emoji.emojize(':fogo:', language='pt'))'''

#Correção

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')
