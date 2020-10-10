#Condição

#if carro.esquerda():
    #bloco True
#else:
    #bloco False

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Seu carro está novo.')
else:
    print('Seu carro está velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')

nome = str(input('Qual é o seu nome? '))
if nome == 'Rodrigo':
    print('Que nome maneiro você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!' .format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) /2
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('SUa média foi ruim! Estude mais!')
print('A sua média foi {:.1f}' .format(m))

#Desafio28 - Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
cp =  randint(0, 5) #faz o computador 'pensar'
from time import sleep
print('-=-' *20 )
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20 )
jogador = int(input('Em que número eu pensei?')) #jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == cp:
    print('Você venceu, parabéns!')
else:
    print('Você perdeu, eu pensei no numero {} e não no {} TENTE NOVAMENTE!' .format(cp, jogador))


#Desafio29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


#Desafio30 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar. 

#Desafio31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. 

#Desafio32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 

#Desafio33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 

#Desafio34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00 calcule um aumento de 10%. Para as inferiores ou iguais, o aumento é de 15%. 

#Desafio35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
