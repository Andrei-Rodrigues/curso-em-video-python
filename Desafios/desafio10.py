#Crie um programa que leia quanto dinheiro
#tem na carteira e mostre quantos dólares
#ela pode comprar.

#Considere
#US$1,00=R$3,27

valorCarteira = float(input('Digite o valor que contém na carteira: '))
dollar = 3.27
qtdDollar = int(valorCarteira / 3.27)
print(qtdDollar)

#Correção

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
