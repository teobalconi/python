from datetime import datetime

nome = 'José Gomes'
idade = 69
altura = 1.98
e_maior = idade > 18
peso = 100
imc = peso / (altura**2)

currentYear = datetime.now().year

if imc <= 18.5:
    condicao = 'magreza'
elif imc > 18.5 and imc<= 24.9:
    condicao = 'normal'
elif imc > 24.9 and imc<= 30:
    condicao = 'sobrepeso'
elif imc > 30:
    condicao = 'sobrepeso'

#print(nome, 'tem', idade, 'anos de idade e seu IMC é: %.2f' % imc, ', portanto sua condição é:', condicao)
print(f'{nome} tem {idade} anos de idade, pesa {peso} kg, seu ano de nascimento é {currentYear - idade} e seu IMC é: {imc:.2f}, portanto sua condição é: {condicao}')

