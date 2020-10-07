#Operações Aritméticas

#ADIÇÃO +
#SUBTRAÇÃO -
#MULTIPLICAÇÃO *
#DIVISÃO /
#POTÊNCIA ou EXPONENCIAÇÃO **
#DIVISÃO INTEIRA //
#MÓDULO ou RESTO DA DIVISÃO %

# = ATRIBUIÇÃO
# == IGUAL Q É USADO EM ARITMÉTICA


#ORDEM DE PRECEDÊNCIA
# 1-> ()
# 2 -> **
# 3 -> *, /, //, % -> FAZ QUEM APARECER PRIMEIRO
# 4 -> +, -
 
# 5+3*2 == 5+6 == 11
# 3*5+4**2 == 3*5+16 == 15+16 == 31
# 3*(5+4)**2 == 3*9**2 == 3*81 == 243


print(int(5+2)) #7
print(int(5-2)) #3
print(int(5*2)) #10
print(int(5/2)) #2.5
print(int(5**2)) #25
print(int(5//2)) #2
print(int(5%2)) #1


nome = input('Digite seu nome:')
print('Prazer em te conhecer, {:20}' .format(nome)) # O nome digitado vai aparecer usando 20 digitos
print('Prazer em te conhecer, {:>20}' .format(nome)) # O nome digitado vai aparecer usando 20 digitos e alinhado à direita
print('Prazer em te conhecer, {:<20}' .format(nome)) # O nome digitado vai aparecer usando 20 digitos e alinhado à esquerda
print('Prazer em te conhecer, {:^20}' .format(nome)) # O nome digitado vai aparecer usando 20 digitos e centralizado
print('Prazer em te conhecer, {:=^20}' .format(nome)) # O nome digitado vai aparecer usando 20 digitos centralzado e colocando sinais de igual(=) nos espaços faltantes

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um outro valor:'))
s = n1+n2
m = n1*n2
sub = n1-n2
d = n1/n2
dint = n1//n2
pot = n1**n2
rest = n1%n2
print('A soma é {}\n a subtração é {}\n a multplicação é {}\n a divisão é {}\n a potência é {}\n a divisão inteira é {}\n o resto é {}.' .format(s, sub, m, d, pot, dint, rest)) #\n == nova linha, quebra de linha sem precisar criar vários prints


#Desafio05 - Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e seu antecessor.

n=int(input('Digite um número:'))
print('O número é {} seu antecessor é {} e seu sucessor é {}' .format(n, n-1, n+1))

#Desafio06 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1=int(input('Digite um número:'))
print('O número é {} \n o dobro é {} \n o triplo é {} \n a raiz quadrada {}' .format(n1, n1*2, n1*3, n1**0.5))

#Desafio07 - Desenvolva um programa que leia as duas notas de um aluno, calcule a mostre a sua média.

nota1=float(input('Digite a nota da sua primeira prova:'))
nota2=float(input('Digite a nota da sua segunda prova:'))
soma= nota1+nota2
print('A média das suas notas é {}' .format(soma/2))

#Desafio08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

vlmetros=float(input('Digite um valor em metros:'))
vlcent = vlmetros * 100
vlmili = vlmetros * 1000
print('Você colocou {}M \n Convertendo em Centimétros:{} \n Convertendo em Milímetro:{} ' .format(vlmetros, vlcent, vlmili))

#Desafio09 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

tab=int(input('Digite um número inteiro:'))
print('O número que você colocou foi {} e sua tabuada é:\n x1: {} \n x2: {} \n x3: {} \n x4: {} \n x5: {} \n x6: {} \n x7: {} \n x8: {} \n x9: {}' .format(tab, tab*1, tab*2, tab*3, tab*4, tab*5, tab*6, tab*7, tab*8, tab*9))

#Desafio10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar (Considere US$=1,00 = R$3,27)

money=float(input('Quantos Reais você tem na sua carteira?'))
dolar=money/3.27

print('Legal, você têm {}R$ e pode cambiar este valor em {}US$' .format(money, dolar))

#Desafio11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pintua uma área de 2 metros quadrados.

larg=int(input('Quantos metros de parede você precisa pintar? Pofavor, primeiro colocar a Largura:'))
alt=int(input('Favor, colocar agora a Altura em metros'))
a=larg*alt
pintar=a/2
print('Você vai precisar de {}litros de tintas para poder pintar {}m quadrados' .format(pintar, a))

#Desafio12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco=float(input('Qual o valor do produto?'))
desc=preco*5/100
final= preco-desc
print('Levando agora, você vai receber 5% de desconto, totalizando {}R$' .format(final))

#Desafio13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo saláro, com 15% de aumento.

atual=float(input('Quanto que você recebe mensalmente no seu trabalho?'))
aumento = atual*15/100
novo = atual+aumento
print('Parabéns você acabou de receber um aumento de 15%, a partir de agora você começará a ganhar {}R$.' .format(novo))
