#Crie um algoritmo que leia um número
#e mostre o seu dobro, triplo e raiz
#quadrada.

print('Verifique o dobro, tripo e a raiz quadrada de um número')
num = int(input('Digite um número: '))
dobro = int(num * 2)
triplo = int(num * 3)
raizQuad = int(num * (1/2))#errado
print('O dobro do número {} é {}'.format(num, dobro))
print('O triplo do número {} é {}'.format(num, triplo))
print('A raiz quadrada do número {} é {}'.format(num, raizQuad))

#Correção do exercício

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (pow(n, (1/2)))))
