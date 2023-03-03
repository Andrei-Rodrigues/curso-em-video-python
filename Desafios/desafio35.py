'''Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou
não formar um triângulo'''

'''print('Verifique se as 3 retas podem formar um triãngulo')

print('')

reta1 = float(input('Digite a largura da primeira reta: '))
reta2 = float(input('Digite a largura da segunda reta: '))
reta3 = float(input('Digite a largura da terceira reta: '))

print('')

if reta1 + reta2 > reta3:
  print('Pode se criar um triângulo')
else:
  print('Não pode se criar um triângulo')'''

#Correção
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima PODEM FORMAR triângulo!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
