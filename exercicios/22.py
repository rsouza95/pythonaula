#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')) .strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}' .format(nome.upper()))
print('Seu nome em letras minúsculas é {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))