#Faça um programa que leia o ano de nascimento de um jovem
#e informe, de acordo com sua idade:

#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo
#que falta ou que passou do prazo.

'''print('Verifique a sua situação com o serviço militar')

print('')

idade = int(input('Digite a sua idade: '))
qnt_temp_falta = 18 - idade
qnt_temp_passou = idade - 18

if idade < 18:
    print('Ainda não é a hora de prestar o serviço militar, falta {} anos'.format(qnt_temp_falta))
elif idade == 18:
    print('Está na hora de prestar o serviço militar')
else:
    print('O tempo de prestar o serviço militar foi à {} anos atrás'.format(qnt_temp_passou))'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alista há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
