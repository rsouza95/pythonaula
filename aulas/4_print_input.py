print('Olá, Mundo!')
print(7+4)
print('7'+'4')

#TODA VARIÁVEL É UM OBJETO
#TODA VARIÁVEL PODE RECEBER(=) VALOR
#PRINT SIGNIFICA ESCREVA
#INPUT SIGNIFICA LEIA

nome = 'Rodrigo'
idade = 25
peso = 140.8

print(nome, idade, peso)


nome = input('Qual é o seu nome?') 
idade = input('Quantos anos você tem?')
peso = input('Qual seu peso?')

#Desafio01 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nome = input('Qual é o seu nome?') 
print('Seja muito bem vindo {}!' .format(nome))

#Desafio02 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

print('Qual sua data de Nascimento?')
Dia = input('Dia')
Mes = input('Mês')
Ano = input('Ano')
print('Você nasceu no dia', Dia, 'de', Mes, 'de', Ano,'.' 'Certo?')

#Desafio03 - Crie um script Python que leia dois números e tente mostrar a soma entre eles.

num1 = int(input('Digite um número'))
num2 = int(input('Digite outro número'))
soma = (num1 + num2)
print('A soma desses números é', soma)