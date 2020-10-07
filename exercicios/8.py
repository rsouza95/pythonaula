#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = (int(input('Digite aqui um valor em metros: ')))
cm = n*100
mm = n*1000
print('O valor que você colocou {}m \n Convertendo para centímetros: {}cm \n Convertendo para milímetros: {}mm' .format(n,cm,mm))