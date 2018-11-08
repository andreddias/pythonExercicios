#Curso Python #014 - Estrutura de repetição while
#só aceite os valores M ou F, caso esteja errado peça digitação
sexo = str(input('Qual é o seu sexo? ').upper())
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Preencha corretamente com M ou F! ').upper())
if (sexo == 'F'):
    print('Você é do sexo feminino!')
else:
    print('Você é do sexo masculino!')
