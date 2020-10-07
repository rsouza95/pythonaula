#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necesśaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a largura da parede que você quer pintar, em metros: '))
altura = float(input('Digite a altura da parede que você deseja pintar, em metros: '))

area = largura*altura
tinta = area/2

print('A área de sua parede é de {}m² e você vai precisar de {}litros de tintas para poder pintá-la' .format(area, tinta))