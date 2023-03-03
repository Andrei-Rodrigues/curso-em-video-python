#Escreva um programa que leia dois números inteiros e compare-os
#mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

'''print('Verifique qual número é maior')

print('')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número é maior')
elif num2 > num1:
    print('O segundo número é maior')
else:
    print('Não existe número maior, os números são iguais')'''

#Correção

n1 = int(input('Primerio número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
