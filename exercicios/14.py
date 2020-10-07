#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

Celsius = float(input('Qual é a atual temperatura, em Celsius, daonde você está?'))
Fah = (Celsius * 9/5) + 32
print('Convertendo {}°C para Fahrenheit, o resultado é de {}°F' .format(Celsius, Fah))
