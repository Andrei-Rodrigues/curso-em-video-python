#A confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Acima: Master

'''print('Verifique a sua categoria')

print('')

idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('Você é um atleta mirim')
elif idade <=14:
    print('Você é um atleta infantil')
elif idade <= 19:
    print('Você é um atleta junior')
elif idade == 20:
    print('Você é um atleta sênior')
else:
    print('Você é um atleta master')'''

#Correção

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
