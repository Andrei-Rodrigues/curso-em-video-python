#Faça um programa que leia a largura e a altura de uma parede
#em metro, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta,
#pinta uma área de 2m quadrados.

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
area = int(largura * altura)
tinta = int(area / 2)
print('A quantidade necessária de tinta para pintar a área de {} metros é {} litros'.format(area, tinta))

#Correção

larg = float(input('Largura da parede: '))
alt = float(input('Altuta da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {} metros quadrados'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
