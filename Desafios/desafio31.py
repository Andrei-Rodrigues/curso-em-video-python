'''Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de de até 200Km
e R$0,45 para viagens mais longas.'''

'''dist = float(input('Digite a distância da viagem: '))
curt = float(dist * 0.50)
long = float(dist * 0.45)

print('')

if dist <= 200:
  print('O valor da viagem é R${:.2f}'.format(curt))
else:
  print('O valor da viagem é R${:.2f}'.format(long))'''

#Correção

distância = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km.'.format(distância))

'''if distância <= 200: #Um modo de definir a condição
  preço = distância * 0.50
else:
  preço = distância * 0.45'''

preço = distância * 0.50 if distância <= 200 else distância * 0.45 #Outro modo de definir a condição

print('E o preço da sua passagem será de R${:.2f}'.format(preço))
