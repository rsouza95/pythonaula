#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kms = int(input('Quantos KM você percorreu com o carro?'))
dias = int(input('Quantos dias você alugou o carro?'))

dia = dias*60
km = kms*0.15
final = dia+km

print('Você precisa pagar R${:.2f}'.format(final))