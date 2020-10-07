#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro qualquer para ver a sua tabuada: '))

# print('O número que você colocou foi {} \n E em seguida vou reproduzir sua tabuada. \n x1: {} \n x2: {} \n x3: {} \n x4: {} \n x5: {} \n x6: {} \n x7: {} \n x8: {} \n x9: {}' .format (n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9))

print('-' *12)
print('{} x {} = {}' .format(n, 1, n*1))
print('{} x {} = {}' .format(n, 2, n*2))
print('{} x {} = {}' .format(n, 3, n*3))
print('{} x {} = {}' .format(n, 4, n*4))
print('{} x {} = {}' .format(n, 5, n*5))
print('{} x {} = {}' .format(n, 6, n*6))
print('{} x {} = {}' .format(n, 7, n*7))
print('{} x {} = {}' .format(n, 8, n*8))
print('{} x {} = {}' .format(n, 9, n*9))
print('-' *12)