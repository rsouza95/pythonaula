#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
al1 = str(input('Qual é o primeiro aluno?'))
al2 = str(input('Qual é o segundo aluno?'))
al3 = str(input('QUal é o terceiro aluno?'))
al4 = str(input('Qual é o quarto aluno?'))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será :')
print(lista)