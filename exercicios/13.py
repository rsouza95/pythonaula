#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o seu salário? R$'))
# aum = sal + (sal*15/100)
aum = sal*15/100
final = sal+aum

print('Parabéns você recebeu um aumento de 15%, seu salário de {:.2f}R$ foi para {:.2f}R$' .format(sal, final))