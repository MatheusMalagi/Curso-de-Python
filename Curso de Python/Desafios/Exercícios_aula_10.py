# EXERCÍCIO 28 - ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSA EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU. 
# import random
# print('Bem vindo ao jogo de adivinhação, aqui você deverá acertar qual é o número que a máquina "pensou"!\nPara te ajudar, o número gerado aleatóriamente sempre será um número inteiro de 0 a 5!\nVamos começar!!')
# numero = random.randint(0, 1)
# chute = int(input('Dê o seu palpite:'))
# # if numero == chute:
# #     print(f'Parabéns, você acertou o número escolhido, que foi o {numero}!')
# # else:
# #     print(f'Que pena, você errou! O número escolhido era o {numero}')

# # OU 

# print(f'Que pena, você errou! O número escolhido era o {numero}' if numero != chute else f'Parabéns, você acertou o número, que foi o {numero}!')



# EXERCÍCIO 29 - ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO, SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO. A MULTA VAI CUSTAR 7 REAIS POR CADA KM A CIMA DO LIMITE
# vel = int(input('Insira a velocidade do carro em Km/h: '))
# if vel > 80:
#     multa = (vel - 80) * 7
#     print(f'Você acabou de ser multado em {multa}')
# else:
#     print(f'Você é um bom motorista e estava a {vel}Km/h')
# OU
# multa = (vel - 80) * 7
# print(f'Você acabou de ser multado em {multa}'  if vel > 80 else f'Você é um bom motorista e estava a {vel} Km/h')


# EXERCÍCIO 30 - CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR
# escolha = int(input('Digite um número: '))
# num = escolha % 2
# # if num == 0:
# #     print(f'O número escolhido foi o {escolha} e ele é PAR!')
# # else:
# #     print(f'O número escolhido foi o {escolha} e ele é IMPAR!')
# #OU
# print(f'O número escolhido foi o {escolha} e ele é PAR!' if num == 0 else f'O número escolhido foi o {escolha} e ele é IMPAR!')

#EXERCÍCIO 31 - CRIE UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO 0,50 CENT POR KM PARA VIAGENS DE ATÉ 200KM E 0,45 CENT PARA VIAGENS MAIS LONGAS.
dist = float(input('Insira a distância da viagem em Km: '))
if dist <= 200:
    preco = dist * 0.50
    print(f'A viagem tem a distância de {dist}Km e a passagem custa R${preco}.')
else:
    preco2 = dist * 0.45
    print(f'A viagem tem a distÂncia de {dist}Km e a passagem custa R${preco2}.')
