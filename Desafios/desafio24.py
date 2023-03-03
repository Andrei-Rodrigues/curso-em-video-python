'''Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "Santo".'''

'''cidade = str(input('Digite o nome de uma cidade: '))
verificar = cidade.startswith('Santo')
print(verificar)'''

#Correção

#Transformou a palavra toda em letra maiúscula e verificou se tem 'Santo' em maiúsculo

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
