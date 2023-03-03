'''Faça um programa que leia o salário de um
funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%'''

'''print('Verifique o aumento do seu salário')

print('')

salario = float(input('Digite o valor do seu salário: '))
maior = salario * 0.1
menor = salario * 0.15

print('')

if salario > 1250.00:
  print('O aumento do seu salário foi de R${}'.format(maior))
else:
  print('O aumento do seu salário foi de R${}'.format(menor))'''

#Correção

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
  novo = salário + (salário * 15 / 100)
else:
  novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
