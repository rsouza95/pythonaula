#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. (Considere US$=1.00 = R$5.63 e EUR6.63 )

real = float(input('Digite aqui, o quanto de dinheiro você tem na carteira: R$'))
dol = real / 5.63
eur = real / 6.63
print('Você tem {:.2f} em R$ \n Cambiando o valor do Real para Dólar você têm US${:.2f} \n Cambiando o valor do real para Euro você tem {:.2f}EUR ' .format(real, dol, eur)) 