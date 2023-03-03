#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
soma = 0
for i in range(1, num + 1):
    if num % i == 0:
        soma = soma + 1
if soma == 2:
    print('É um número primo')
else:
    print('Não é um número primo')
