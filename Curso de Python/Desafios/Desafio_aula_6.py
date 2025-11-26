#desafio 01 - criar um programa que le dois numeros e mostra a soma entre eles

print('SOMA')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
s = n1 + n2
print(f'A soma de {n1} e {n2} é igual a {s}')

print('SUBTRAÇÃO')
s = n1 - n2
print(f'A subtração de {n1} e {n2} é igual a {s}')

print('MULTIPLICAÇÃO')
s = n1 * n2
print(f'A multiplicação de {n1} e {n2} é igual a {s}')

print('DIVISÃO')
s = n1 / n2
print(f'A divisão de {n1} e {n2} é igual a {s}')

#desafio 02 - faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

v = input('Digite algo: ')
print('O tipo primitivo do que você digitou é: ', type(v))
print('O que você digitou é alpha numérico? > ', v.isalnum())
print('O que você digitou é alfabético? > ', v.isalpha())
print('O que você digitou é decimal? > ', v.isdecimal())
print('O que você digitou está em minúsculo? > ', v.islower())
print('O que você digitou está em maiúsculo > ', v.isupper())

# exemplo com format
print(f'Conferência do que foi digitado numérico {v.isalnum()}, alfabético {v.isalpha()}' )



