#Faça um Programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, cos, tan, sin
ang = float(input('Digite um ângulo qualquer: '))
cosseno = cos(radians(ang))
seno = sin(radians(ang))
tangente = tan(radians(ang))
print('O ângulo {} tem o cosseno de {:.2f}' .format(ang, cosseno))
print('O ângulo {} tem o seno de {:.2f}' .format(ang, seno))
print('O ângulo {} tem a tangente de {:.2f}' .format(ang, tangente))
