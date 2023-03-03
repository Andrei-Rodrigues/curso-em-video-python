#Escreva um programa para aprovar o empréstimo bancário
#para a compra de uma casa. O programa vai perguntar o
#valor da casa, o salário do comprador e em quantos anos
#ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não
#pode exceder 30% do salário ou então o empréstimo será negado.

'''print('Validação de empréstimo')

valor_casa = float(input('Qual é o valor da casa? '))
salario_comprador = float(input('Qual é o seu salário? '))
anos_pagamento = int(input('Quantos anos de pagamento? '))

pag_mensal = float(valor_casa / (12 * anos_pagamento))
valor_disp_mensal = float(salario_comprador * (30/100))

print(valor_disp_mensal)

print('O valor da parcela será de R${:.2f}'.format(pag_mensal))

if pag_mensal > valor_disp_mensal:
    print('\033[31mSinto muito, o empréstimo não foi aprovado\033[m')
elif pag_mensal < valor_disp_mensal:
    print('\033[32mParabéns! O seu empréstimo foi aprovado\033[m')'''

#Correção

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))

if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
