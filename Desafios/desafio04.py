#Faça um programa que leia algo pelo teclado e
#mostre na tela o seu tipo primitivo e todas as
#informações possíveis sobre ele.

valor = input('Digite alguma coisa')
print('O tipo primitivo desse valor é', type(valor))
print('É somente espaço?', (valor.isspace()))
print('É um número?', (valor.isnumeric()))
print('É alfabético?', (valor.isalpha()))
print('É alfanumérico', (valor.isalnum()))
print('É em letras maiúsculas?', (valor.isupper()))
print('É em letras minúsculas?', (valor.islower()))
print('Está capitalizada?', (valor.istitle()))

