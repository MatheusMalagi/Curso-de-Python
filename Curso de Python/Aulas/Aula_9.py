#MANIPULAÇÃO DE TEXTO
# [] > representa uma lista no python

# FATIAMENTO

# se usarmos um print(frase[]) se colocarmos um número no meio do [] nós iremos fatiar a string, fazendo aparecer somente a letra que aquele número representa
# devemos sempre lembrar que a primeira letra da frase começa em 0, os espaços entre as palavras também contam como número.
#EXEMPLOS
frase = 'Curso em Vídeo Python'
print(frase[9])

# assim você seleciona da cadeia 9 a 12, ele para de contar no 13 mas não pega ele. 
frase = 'Curso em Vídeo Python'
print(frase[9:13])

# a frase tem cadeia até o 20 mas colocamos para pegar do 9 ao 21, mesmo não tem 21 ele pegará até o 20
frase = 'Curso em Vídeo Python'
print(frase[9:21])

#começa no 9 e salta de 2  em 2 do 9 ao 21
frase = 'Curso em Vídeo Python'
print(frase[9:13:2])

#começa do caractere inicial e para na letra 5 que na verdade é 4
frase = 'Curso em Vídeo Python'
print(frase[:5])

#começa no 15 e vai até o final da string
frase = 'Curso em Vídeo Python'
print(frase[15:])

# começa no 9 e vai até o final, porém como ele tem o :3 ele pula de 3 em 3 mostrando somente alguns caracteres
frase = 'Curso em Vídeo Python'
print(frase[9::3])

#ANALISE
#mostra a quantidade de caracteres na string
frase = 'Curso em Vídeo Python'
print(len(frase))

#pede para contar quantas vezes existe a letra 'o' na frase
frase = 'Curso em Vídeo Python'
print(frase.count('o'))

#conta os 'o' na frase e ja fatia a frase, dizendo que do caractere 0 ao 13 somente tem uma letra 'o'
frase = 'Curso em Vídeo Python'
print(frase.count('o',0,13))

#mostra em que posição começou o 'deo' na frase
frase = 'Curso em Vídeo Python'
print(frase.fin('deo'))

#se colocamos no find uma string que não existe o valor retornado irá ser -1
frase = 'Curso em Vídeo Python'
print(frase.find('Android'))

#Existe Curso na frase? Sim, então ele retornará "True" na tela
'Curso' in frase

#TRANSFORMAÇÃO
#Substitui de forma secundária uma palavra na string
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))

#O que for maiusculo ele mantem e o que não for ele coloca em maiusculo
frase = 'Curso em Vídeo Python'
print(frase.upper())

#faz a mesma coisa que a anterior so que com letras minusculas
frase = 'Curso em Vídeo Python'
print(frase.lower())

#deixa somente a primeira letra da string em minusculo
frase = 'Curso em Vídeo Python'
print(frase.capitalize())

#analisa a string através dos espaços entre as palavras e coloca a primeira letra de cada palavra em maiuscula
frase = 'Curso em Vídeo Python'
print(frase.title())

#TRANSFORMAÇÃO
#remove todos os espaços inúteis do começo e do final da string
frase = 'Curso em Vídeo Python'
print(frase.strip())

#remove somente os espaços inuteis do lado direito da string
frase = 'Curso em Vídeo Python'
print(frase.rstrip())

#remove somente os espaços inuteis do lado esquerdo da string
frase = 'Curso em Vídeo Python'
print(frase.lstrip())

#DIVISÃO
#divide a strig considerando os espaços, onde tiver espaço na string ele faz uma divisão colocando cada palavra em uma outra lista
frase = 'Curso em Vídeo Python'
print(frase.split())

#JUNÇÃO
#substitui os espaços por '-'
frase = 'Curso em Vídeo Python'
print('-'.join(frase))




