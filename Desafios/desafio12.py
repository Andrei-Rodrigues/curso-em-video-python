#Faça um algoritmo que leia o preço
#de um produto e mostre seu novo preço
#com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
valor = float(preco * (5/100))
print(valor)

#Correção

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
