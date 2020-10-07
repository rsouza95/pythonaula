
#TIPOS PRIMITIVOS - #INT(Números Inteiros)(7,-4,0,9875) - #FLOAT(Números Reais)(4.5, 0.076, -15.223, 7.0) - #BOOL(Valores Lógicos)(True=Verdadeiro, False=Falso) - #STR(String=Caracteres)('Olá','7.5', '')


n1=int(input('Digite um número:'))
print(type(n1))
n2=int(input('Digite outro número:'))
soma=n1+n2

#print('A soma de', n1, 'e de', n2, 'é: ' , soma)

#print('A soma de {0} e {1} é: {2}' .format(n1, n2, soma))

#print('A soma desses dois números é:', soma)

#print('A soma desses dois números é: {}!' .format(soma))

n = float(input('Digite um valor: '))
print(n)

nx = str(input('Digite um valor:'))
print(nx)

ny = bool(input('Digite um valor:'))
print(ny)

nz = input('Digite algo:')
print(nz.isnumeric())
# É NÚMERICO?

nw = input('Digite algo:')
print(nw.isalpha())
# É ALFABÉTICO?

nj = input('Digite algo:')
print(nj.isalnum())
# É ALFANÚMERICO?

nk = input('Digite algo:')
print(nk.isupper())
#ESTÁ EM LETRAS MAIÚSCULAS?


#Desafio03* - Crie um programa que leia dois números e mostre a soma entre eles.
n3=int(input('Digite um número:'))
n4=int(input('Digite um outro número:'))
soma2=n3+n4
print('A some entre os dois números que você colocou é:', soma2)

print('A soma entre {} e {} tem como resultado: {}' .format(n3, n4, soma2))


#Desafio04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
x=input('Digite algo:')
print(type(x))
print('É um elemento Alfanúmerico?', x.isalnum())
print('É um alfabeto?', x.isalpha())
print('É um número?', x.isnumeric())
print('Está com letra maiúscula?', x.isupper())
print('Está com letra minúscula?', x.islower())
print('É um número decimal?', x.isdecimal())
print('É um espaço', x.isspace())