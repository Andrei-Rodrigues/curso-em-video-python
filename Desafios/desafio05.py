#Faça um programa que leia um número
#inteiro e mostre na tela o seu sucessor
#e seu antecessor.

numeroInt = int(input('Digite um número inteiro para verificar o seu sucessor e antecessor: '))
suc = int(numeroInt + 1)
ant = int(numeroInt - 1)
print('O sucessor do número {} é {}'.format(numeroInt, suc))
print('O antecessor do número {} é {}'.format(numeroInt, ant))

#Outra maneira de ser feito (maneira feita na correção)

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n+1)))
