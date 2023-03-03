#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

'''from datetime import date

data = date.today().year

totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nasc = int(input('{}° pessoa - digite o ano de nascimento: '.format(pessoas)))
    idade = data - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('A quantidade de pessoas maiores de idade é {}'.format(totmaior))
print('A quantidade de pessoas menores de idade é {}'.format(totmenor))'''

#Correção

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
