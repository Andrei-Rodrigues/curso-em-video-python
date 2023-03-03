#Crie um programa que leia duas notas de um aluno e calcule
#sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#Média abaixo de 5.0:
#Reprovado

#Média entre 5.0 e 6.9:
#Recuperação

#Média 7.0 ou superior:
#Aprovado

'''print('Verifique se você foi aprovado')

print('')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Você foi reprovado')
elif media < 6.9:
    print('Você está em recuperação')
else:
    print('Você foi aprovado')'''

#Correção

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))

if média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO')
elif média < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está APROVADO')
