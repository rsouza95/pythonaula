frase = 'Curso em Video Python'

#Fatiamento - #Range o ultimo valor não entra na contagem - [10:13] -> [10, 11, 12]
frase[9:21]
frase[9:21:(2)] # Saltando de dois em dois
frase[:5] # Antes dos : é aonde ele vai começar, caso eu não coloque aonde ele vai começar, ele vai começar do caractere 0(do ínicio).
frase[15:] # Depos dos : é aonde ele vai terminar, caso eu não coloque aonde ele vai terminar, vai terminar no último caractere.
frase[9::3] # Começar no 9 e vai até o final, como depois do primeiro dois pontos tem uma omissão de elemento o fatiamento vai continuar até o final. Sobrando o ':3', vai ser preciso saltar a frase de 3 em 3 'casas'.

#Análise -#len (length) == comprimento.
#len(frase)
frase.count('o') #contar quantas letras 'o' minúscula.
print(frase.count('o'))
frase.count('o', 0, 13) #contagem já com o fatiamento.
print(frase.count('o', 0, 13))

frase.find('deo') #quantos vezes ele encontrou 'deo'.
frase.find('Android') #vai retornar o valor -1, significa que a string 'Android' não existe na frase.
'Curso' in frase # True

#Transformação - uma lista de string é imutável, mas podemos mudar através dos métodos.
frase.replace('Python','Android') #Trocar - vai procurar por 'Python' e vai substituir por 'Android'.
frase.upper() #Deixa a frase inteira maiúscula.
frase.lower() #Deixa a frase inteira minúscula.
frase.capitalize() #Joga todos os caracteres para minúsculos e só o primeiro caractere vai ficar maiúsculo.
frase.title() #Vai analisar quantas palavras tem nessa string, aonde tiver espaço na string vai haver uma quebra de palavra, e ele vai fazer o capitalize palavra por palavra.

frase2 = '   Aprenda Python  '
frase2.strip( ) #'Vai remover todos os espaços inúteis no ínicio e no final da string, lembrando q o espaço do meio vai ser mantido.
print(frase2.strip)
frase2.rstrip() #r=right - vai remover somente os espaços do lado direito da string.
frase2.lstrip() #l=left - vai remover somente os espaços do lado esquerdo da string.

#Divisão
frase = 'Curso em Video Python'
frase.split() #Vai ocorrrer uma divisão dentro da string, considerando os espaços.
str(print(frase.split()))
#Junção
' '.join(frase)
minhafrase = ('Curso','em', 'Video', 'Python')
x = '#' .join(minhafrase)
print(x)

#Prática

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('Oi')
print("""Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why
 and how to get started with Python. Fortunately an experienced programmer in any programming language whatever it may be 
 can pick up Python very quickly. Its also easy for beginners to use and learn, so jump in!""")
print(frase.count('o'))
print(frase.upper().count('O'))
teste_frase = '                Curso em Vídeo Python                  '
print(len(teste_frase))
print(len(teste_frase.strip()))

print(frase.replace('Python', 'Android'))

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])


#Desafio22 - Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome.

nome = str(input('Qual é o seu nome completo?')) .strip()
str(print('Com todas as letras maiúsculas o seu nome ficará desta forma: {} '.format (nome.upper() )))
str(print('Com todas as letras minúsculas o seu nome ficará desta forma: {}'.format (nome.lower() )))
str(print('O seu nome tem {} letras desconsiderando os espaços.' .format (len(nome) - nome.count(' '))))
str(print('O seu primeiro nome tem {} letras' .format(nome.find(' '))))

#Desafio23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. EX: Digite um número: 1834 UNIDADE:4 DEZENA:3 CENTENA:8 MILHAR:1
 
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O milhar deste número é: {}' .format(m))
print('A centena deste numero é: {}' .format(c))
print('A dezena deste número é: {}' .format(d))
print('A unidade deste número é: {}' .format(u))

#Desafio24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cidade = str(input('Qual o nome da sua cidade?')) .strip()
print(cidade[:5].upper() == 'SANTO')

#Desafio25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = str(input('Qual é o seu nome completo?'))
print('Seu nome tem Silva? {}' .format('SILVA' in nome.upper()))

#Desafio26 - Faça um programa que leia uma frase pelo teclado e mostre: - Quantas vezes aparece a letra 'A'. Em que posição ela aparece a primeira vez. Em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')) .upper() .strip()
print('Nesta frase, a letra A apareceu {} vezes' .format(frase.count('A')))
print('A primeira letra A apareceu na posição {}' .format(frase.find('A') +1 ))
print('A última letra A apareceu na posição {}' .format(frase.rfind('A') +1))

#Desafio27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza. Primeiro = Ana , último = Souza

n = str(input('Digite o seu nome completo: ')) .strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nomé é {}' .format(nome[0]))
print('Seu último nome é {}' .format(nome[len(nome)-1]))


