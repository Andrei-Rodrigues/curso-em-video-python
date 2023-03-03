#Escreva um programa que leia um valor em metro e o
#exiba convertido em centímetros e milímetros.

metros = int(input('Digite uma metragem: '))
cen = metros * 100
mil = metros * 1000
print('A metragem {} é {} em centímetros'.format(metros, cen))
print('A metragem {} é {} em milímetros'.format(metros, mil))

#Correção

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A média de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))