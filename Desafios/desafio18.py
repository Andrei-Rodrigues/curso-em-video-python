#Faça um programa que leia um angulo
#qualquer e mostre na tela o valor
#do seno, cosseno e tangente
#desse angulo.
#28:50 aula 08

'''import math

print('Digite o cateto adjacente e oposto e verifique o resultado de seno, cosseno e tangente')

print('')

cat_op = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))

print('')

cal_hip = (cat_op ** 2) + (cat_adj ** 2)
result_hip = math.sqrt(cal_hip)

seno = cat_op/result_hip
cosseno = cat_adj/result_hip
tangente = cat_op/cat_adj

print('O valor de seno é {:.2f}'.format(seno))
print('O valor de cosseno é {:.2f}'.format(cosseno))
print('O valor da tangente é {:.2f}'.format(tangente))'''


#Correção

from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO DE {:.2f}'.format(ângulo, seno))

cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
