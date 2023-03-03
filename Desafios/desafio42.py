#Refaça o DESAFIO 035 dos triãngulos, acrescentando
#o recurso de mostrar que tipo de triângulo será formado:

#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

'''print('Verifique quais dos três tipos de triângulo representa: Equilátero, Isósceles ou Escaleno.')

print('')

lado1 = float(input('Digite a largura do primeiro lado: '))
lado2 = float(input('Digite a largura do segundo lado: '))
lado3 = float(input('Digite a largura do terceiro lado: '))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Triângulo Equilátero')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')'''

#Correção

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
  if r1 == r2 == r3:
    print('EQUILÁTERO')
  elif r1 != r2 != r3 !=r1:
    print('ESCALENO')
  else:
    print('ISÓSCELES')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
