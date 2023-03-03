#Desenvolva um programa que leia seis números inteiros e mostra a soma
#apenas daquele que forem pares. Se o valor digitado for ímpar, desconsidere-0.

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('A soma total dos {} números pares é {}'.format(cont, soma))
