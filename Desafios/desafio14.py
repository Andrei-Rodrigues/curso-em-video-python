#Escreva um programa que converta uma temperatura
#digitada em celsius e converta para fahrenheit

#F = C x 1,8 + 32

celsius = float(input('Digite a temperatura em celsius para verificar em fahrenheit: '))
fahrenheit = 1.8 * celsius + 32
print('A tempera {}C° graus celsius equivale a {}°F'.format(celsius, fahrenheit))
