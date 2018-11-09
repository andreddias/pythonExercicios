#leia o peso e a altura e calcule seu imc
#18.5 abaixo do peso
#entre 18.5 e 25 ideal
#25 até 30 sobrepeso
#30 até 40 obesidade
#acima de 40 obesidade morbida

peso = float (input('Digite o seu peso: '))
altura = float (input('Digite a sua altura? '))

imc = peso / (altura ** 2)

print('Seu imc é {:.1f}'.format(imc))

if (imc < 18.5):
    print('O seu IMC está abaixo de 18.5, portanto você está abaixo do peso')
elif (imc >= 18.5 and imc < 25):
    print('Você está no peso ideal')
elif (imc >= 25 and imc < 30):
    print('Você está com sobrepeso')
elif (imc >= 30 and 40):
    print('O seu IMC está entre 30 e 35. Isto significa que está situado na categoria de obesidade moderada.')
elif (imc > 40):
    print('Seu imc é {} Obesidade mórbida'.format(imc))
