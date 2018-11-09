#Exercício Python #033 - Maior e menor valores
#faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro de 3 números: '))
n2 = int(input('Digite o segundo de 3 números: '))
n3 = int(input('Digite o último de 3 números: '))

menor = n1

if (n2 < n1) and (n2 < n3):
    menor = n2
if (n3 < n1) and (n3 < n2):
    menor = n3
print('o menor número é {}'.format(menor))

maior = n1
if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n1) and (n3 > n2):
    maior = n3
print('O maior número é {}'.format(maior))
