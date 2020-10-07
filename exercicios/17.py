#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catop = float(input('Qual é o comprimento do cateto oposto? '))
catadj = float(input('Qual é o comprimento do cateto adjacente? '))
hip = hypot(catop, catadj)
print('O hipotenusa deste triângulo mede {:.2f}m²'.format(hip))