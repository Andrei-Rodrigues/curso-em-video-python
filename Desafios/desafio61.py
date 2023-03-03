#Refaça o DESAFIO 051, lendo o primeira termo e a razão de uma PA, mostrando os 10 primeiros
#termos da progressão usando a estrutura while.

print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
