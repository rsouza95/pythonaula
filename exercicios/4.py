x=input('Digite algo:')
print('Tipo primitivo dsse valor é', type(x))
print('É um elemento alfanúmerico?:', x.isalnum())
print('É um número?:', x.isnumeric())
print('É um número decimal?' , x.isdecimal())
print('É um alfabeto:?', x.isalpha())
print('Está totalmente em maiúsculo?', x.isupper())
print('Está totalmente em minúsculo?', x.islower())
print('Está capitalizada?', x.istitle()) #CAPITALIZADA = MAIÚSCULA NA PRIMEIRA LETRA
print('Só tem espaços?', x.isspace())

