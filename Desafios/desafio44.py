#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

'''produto = float(input('Digite o valor do produto: R$'))

print('')

print('Digite 1 - Para pagamento a vista ou em cheque')
print('Digite 2 - Para pagamento no cartão')
print('Digite 3 - Para pagamento em até 2x no cartão')
print('Digite 4 - Para pagamento em até 3x ou mais no cartão')

print('')

pagamento = int(input('Forma de pagamento: '))

print('')

if pagamento == 1:
    valor = produto * (10 / 100)
    valor_final = produto - valor
    print('O valor do produto será R${:.2f}'.format(valor_final))

elif pagamento == 2:
    valor = produto * (5 / 100)
    valor_final = produto - valor
    print('O valor do produto será R${:.2f}'.format(valor_final))

elif pagamento == 3:
    valor = produto
    valor_mes = produto / 2
    print('O total do pagamento vai ser R${:.2f}, R${:.2f} por mês'.format(valor, valor_mes))

elif pagamento == 4:
    valor_juros = produto * (20 / 100)
    valor_final = produto + valor_juros
    qtd_vezes = int(input('Digite a quantidade de vezes para pagamento: '))
    valor_mes = valor_final / qtd_vezes
    print('O total do pagamento vai ser R${:.2f}, R${:.2f} por mês'.format(valor_final, valor_mes))'''

#Correção

print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - ( preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de  pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
