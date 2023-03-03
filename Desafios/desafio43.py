#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule
#seu IMC e mostre seu status, de acordo com a tabela abaixo:

#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

'''peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('O seu IMC é {:.2f} - Classificação - Abaixo do peso'.format(imc))
elif imc < 25:
    print('O seu IMC é {:.2f} - Classificação - Peso ideal'.format(imc))
elif imc < 30:
    print('O seu IMC é {:.2f} - Classificação - Sobrepeso'.format(imc))
elif imc < 41:
    print('O seu IMC é {:.2f} - Classificação - Obesidade'.format(imc))
else:
    print('O seu IMC é {:.2f} - Classificação - Obesidade mórbida'.format(imc))'''

#Correção

peso = float(input('Qual é o seu peso: (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso /(altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, Você está na faixa de peso PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO')
elif imc >= 30  and imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado')
