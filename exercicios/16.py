#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. (Ex: 6.127 -> 6)

from math import trunc
n = float(input('Digite aqui um número Real qualquer: '))
print('Você digitou o número {} \n Sua porção inteira é: {}' .format(n, trunc(n)))