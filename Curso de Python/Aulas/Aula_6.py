#Tipos primitivos, devem ser especificados na variável ou no momento em que o comando irá ser lido

#int = numeros inteiros
#float = números reais, que tem vírgula (pode ser inteiro se for por ex: 7,0)
#bool =  somente aceita "True" ou "False" sempre usar com letras minusculas inicialmente
#str = sempre estarão entre '' para indicar que são caracteres

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma entre  {} e {}, é de: {}'.format(n1, n2, s))

#outros jeitos de escrever a mesma coisa do primeiro print

print(f'A soma entre  {n1} e {n2}, é de: {s}')

print('A soma entre', n1, 'e', n2, f'é de: {s}')

#outra parte da aula
