# Exercício original: Python #006 - Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
# Esse exercício foi atualizado com a inclusão dos outros operadores da aula 07 - Operadores Aritméticos

n = int(input('Digite um número: '))
print('O dobro de {} é {}.'.format(n, (n*2)))
print('O triplo de {} é {}. \nA raiz quadrada de {} é {}'.format(n, (n*3), n, (n**(1/2))))
print('O número {} elevado ao quadrado é {}'.format(n, n**2))
print('A metade de {} é {}'.format(n, (n/2)))
print('{} dividido por 2 é {}'.format(n, (n//2)))
resto = n%2
if (resto != 0):
    print('o resto da divisão de {} por 2 é {}'.format(n, resto))
