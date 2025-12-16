import math, random

#EXERCICIO 16 - PROGRAMA QUE LE UM NÚMERO REAL E MOSTRA A PARTE INTEIRA
# num = float(input('Escreva um número com vírgula: '))
# nsv = math.trunc(num)
# print(f'O número escolhido foi {num} e a parte inteira dele é {nsv}')

#EXERCICIO 17 - CALCULAR A HIPOTENUSA DE UM TRIANGULO RETANGULO
# cat_op = float(input('Informe o valor do cateto oposto: '))
# cat_ad = float(input('Informe o valor do cateto adjacente: '))
# hip = math.sqrt(pow(cat_op, 2) + pow(cat_ad, 2))
# print(f'A hipotenusa do triangulo retangulo é {hip:.2f}')

#EXERCICIO 18 - PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DO ANGULO.
# num = float(input('Informe um angulo qualquer: '))
# ang = math.radians(num)
# cos = math.cos(ang)
# sen = math.sin(ang)
# tan = math.tan(ang)
# print(f'O angulo é de {num:.0f}°, seu cosseno é {cos:.2f}, o seno é {sen:.2f} e a tangente é {tan:.2f}')

#EXECICIO 19 - SORTEAR UM DOS ALUNOS PARA APAGAR O QUADRO. PROGRAMA QUE AJUDA O PROFESSOR, LENDO O NOME DOS ALUNOS E ESCREVENDO O NOME DO ESCOLHIDO
# aluno = random.choice(['Carlos','Eduardo','Mônica','Roberta','Dagoberto'])
# print(f'O aluno(a) que irá apagar o quadro hoje é: {aluno}')

# MANEIRA QUE O GUANABARA QUERIA:
# a1 = input('Primeiro aluno: ')
# a2 = input('Segundo aluno: ')
# a3 = input('Terceiro aluno: ')
# a4 = input('Quarto aluno: ')
# lista = [a1, a2, a3, a4]
# escolhido = random.choice(lista)
# print(f'O aluno escolhido para apagar a lousa foi o(a): {escolhido}')

#EXERCICIO 20 - MESMA COISA DO EX ANTERIOR, MAS O SORTEIO SERVIRÁ PARA ESCOLHER A ORDEM DE APRESENTAÇÃO DOS TRABALHOS, O SORTEIO DEVE MOSTRAR O NOME DOS QUATRO ALUNOS E A ORDEM DE SORTEIO
# aluno = random.sample(['Carlos','Eduardo','Mônica','Roberta','Dagoberto'], k=5)
# print(f'A ordem de apresentação dos trabalhos será: {aluno}')

# MANEIRA QUE O GUANABARA QUERIA:
# a1 = input('Primeiro aluno: ')
# a2 = input('Segundo aluno ')
# a3 = input('Terceiro aluno: ')
# a4 = input('Quarto aluno: ')
# lista = [a1, a2, a3, a4]
# random.shuffle(lista)
# print('A ordem de apresentação dos trabalhos será')
# print(lista)


#EXERCICIO 21 - FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
#ver com o jarabara
#até tentei instalar o pygame, mas essa porcaria não tocou o áudio, então eu desisti desse
# import pygame
# pygame.init()
# pygame.mixer.music.load('vanessa.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()








