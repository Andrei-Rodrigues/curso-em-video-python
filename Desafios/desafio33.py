'''Faça um programa que leia três números e mostre
qual é o maior e qual é o menor.'''

'''print('Verifique quel número é maior')

print('')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

print('')

if num1 > num2 and num1 > num3:
  print('O primeiro número é maior')
elif num2 > num3:
  print('O segundo número é maior')
else:
  print('O terceiro número é maior')'''

#Correção

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando que é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando que é o maior
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
