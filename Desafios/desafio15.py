#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
#que o carro custa R$60 por dia e R$0,15 por km rodado.


qtd_km = float(input('Qual foi a quilometragem percorrida? '))
qtd_dia = int(input('Foram quantas diárias de aluguel? '))

print()

print('A quilometragem percorrida foi de {}km'.format(qtd_km))
print('Foram {} diárias utilizadas'.format(qtd_dia))

print()

valor_diaria = qtd_dia * 60
valor_km = qtd_km * 0.15
valor_servico = valor_diaria + valor_km

print('O valor do serviço foi de R${:.2f}'.format(valor_servico))
