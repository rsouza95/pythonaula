# import bebidas # vai importar todas as bebidas
#from doces import pudim # vai importar só o pudim

#math - módulo básico das operações matemática
#ceil -> arredondamento para cima
#floor -> arredondamento para baixo
#trunc -> eliminar da vírgula para frente, sem fazer arredondamento
#pow -> potência == **
#sqrt -> calcular raiz quadrada (squareroot)
#factorial -> calcular fatorial de um número

#import math # vai importar todas funções de math!

#from math import sqrt, ceil # importar somente sqrt e ceil

import math
num1 = int(input('Digite um número: '))
raiz = math.sqrt(num1)
print('A raiz de {} é igual {:.2f}' .format(num1, raiz))


from math import sqrt, floor
num2 = int(input('Digite um número: '))
raiz = sqrt(num2)
print('A raiz de {} é igual {:.2f}' .format(num2, floor(raiz)))

import random
num3 = random.randint(1,10)
print(num3)

#Desafio16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: 6.127 -> 6

from math import trunc
num4 = float(input('Digite um número real qualquer: '))
print('A sua porção inteira é {}' .format (trunc(num4)))

#Desafio17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#quadrado da hipotenusa = soma dos quadrados dos catetos


catop = float(input('Qual é o comprimento do Cateto Oposto? '))
catadj = float(input('Qual é o comprimento do Cateto Adjacente? '))
hip = (catop ** 2 + catadj ** 2) ** 0.50
print('O comprimento desta hipotenusa é de {:.2f}m²' .format(hip)) 

from math import hypot
catop = float(input('Qual é o comprimento do Cateto Oposto? '))
catadj = float(input('Qual é o comprimento do Cateto Adjacente? '))
hip = math.hypot(catop, catadj)
print('O comprimento desta hipotenusa é de {:.2f}m²' .format(hip))



#Desafio18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = float(input('Digite o valor de um ângulo qualquer: '))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
seno = sin(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}' .format(ang, seno))
print('O ângulo de {} tem o cosseno de {:.2f}' .format(ang, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}' .format(ang, tangente))

#Desafio19 - UM professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
al1 = str(input('Digite aqui o nome do seu primeiro aluno: '))
al2 = str(input('Digite aqui o nome do seu segundo aluno: '))
al3 = str(input('Digite aqui o nome do seu terceiro aluno '))
al4 = str(input('Digite aqui o nome do seu quarto aluno: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O(a) aluno(a) {} foi escolhido(a) para apagar o quadro.' .format(escolhido))

#Desafio20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
alu1 = input('Digite aqui o nome do seu primeiro aluno: ')
alu2 = input('Digite aqui o nome do seu segundo aluno: ')
alu3 = input('Digite aqui o nome do seu terceiro aluno: ')
alu4 = input('Digite aqui o nome do seu quarto aluno: ')
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)
print('A ordem sorteada foi: ')
print(lista)

#Desafio21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

