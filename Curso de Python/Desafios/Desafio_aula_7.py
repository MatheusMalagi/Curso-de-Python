# Exercício 5 - predecessor e sucessor de um número

# n = int(input("Escolha um número: "))
# p = n - 1
# s = n + 1
# print(f"O número predecessor de {n} é {n}, e o sucessor de {n} é {n}!" )

# Exercício 6 - dobro, triplo e raiz de um número

# n2 = int(input('Escolha um número: '))
# d = n2 * 2
# t = n2 * 3
# r = n2 ** (1/2)
# print(f'O dobro de {n2} é {d}, enquanto o triplo de {n2} é {t}. Já a raiz quadrada de {n2} é igual a {r}!')

# Exercício 7 - média de duas notas

# n1 = float(input('Informe a primeira nota: '))
# n2 = float(input('Informe a segunda nota: '))
# m = (n1 + n2) / 2
# print(f'A média final da soma de {n1} + {n2} é igual a {m}')

# Exercício 8 - programa que le os valores em metros e exibe em centímetro e milímetros

# m = float(input('Insira uma medida em metros: '))
# c = m * 100
# mm = m * 1000
# print(f'{m} metros ao convertermos para centímetros fica {c} cm, que em milímetros fica {mm} mm!')

# Exercício 9 - tabuada

# n = int(input('Escolha um número para calcular a tabuada: '))
# n1 = n * 1
# n2 = n * 2
# n3 = n * 3
# n4 = n * 4
# n5 = n * 5
# n6 = n * 6
# n7 = n * 7
# n8 = n * 8
# n9 = n * 9
# n10 = n * 10
# print(f'{n} x 1 = {n1}')
# print(f'{n} x 2 = {n2}')
# print(f'{n} x 3 = {n3}')
# print(f'{n} x 4 = {n4}')
# print(f'{n} x 5 = {n5}')
# print(f'{n} x 6 = {n6}')
# print(f'{n} x 7 = {n7}')
# print(f'{n} x 8 = {n8}')
# print(f'{n} x 9 = {n9}')
# print(f'{n} x 10 = {n10}')

# Exercício 10 - programa que le quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
# Considerando que U$1 = R$ 3,27 > 1 / 3,27 = 0,305

# c = float(input('Insira quantos reais você possui: R$'))
# d = c / 3.27
# print(f'Com R${c} você tem U${d} !')

# Exercício 11 - fazer um programa que le a largura e a altura de uma parede em metro e calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

# larg = float(input('Informe a largura da parede em metros: '))
# alt = float(input('Informe a altura da parede em metros: '))
# area = larg * alt
# lit = area / 2
# print(f'A parede possui {area} m² e a quantidade de tinta que será utilizada é de {lit} Litros!')

# Exercício 12 - fazer um algoritmo que le o preço de um produto e mostra o novo preço com os 5% de desconto

# p = float(input('Qual é o preço do item: '))
# d = p * 0.05 
# pf = p - d
# print(f'O preço inicial do produto foi de {p} reais, o desconto de 5% é de {d} reais, que faz o preço final ser {pf} reais!')

# Exercício 13 -  faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

# s = float(input('Insira o seu salário atual: '))
# aum = s * 0.15
# sf = s + aum
# print(f'O salário final com o aumento de 15% será de {sf} reais, um aumento de {aum} reais!')

# Exercício 14 -  conversor de grau celsius para Farenheit

# celsius = float(input('Insira quantos graus celsius está fazendo: '))
# fahrenheit = celsius * 1.8 + 32
# kelvin = celsius + 273.15
# print(f'A temperatura em Celsius é de {celsius}, que em Fahrenheit é {fahrenheit} e que em Kelvin é {kelvin}.')

# Exercício 15 -  aluguel de carro, calcular o preço a pagar sabendo que o carro custa 60 reais por dia e 0.15 centavos por km rodado. Programa deve perguntar a quantidade de km percorridos e a quantidade de dias que foi alugado.

dias = int(input('Insira quantos dias você permaneceu com o carro alugado: '))
km = float(input('Insira quantos quilômetros foram percorridos com o carro: '))
preçoDia = dias * 60
kmPreço = km * 0.15
preçoTotal = preçoDia + kmPreço
#calculo reduzido > preçoTotal = (dias * 60) + (km * 0.15)
print(f'O preço total do aluguel é de R${preçoTotal}.\nVocê ficou {dias} dias com o veículo totalizando R${preçoDia} e percorreu {km}Km que totalizou R${kmPreço}.')