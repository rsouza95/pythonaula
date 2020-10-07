#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. Com 5% de desconto.

prod = float(input('Qual o valor deste produto? R$'))
desc = prod*5/100
final = prod-desc
print('Com o desconto de 5% o valor final será R${:.2f}'.format(final))