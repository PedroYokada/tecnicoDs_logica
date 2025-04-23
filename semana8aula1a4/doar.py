idade = int(input('Insira a sua idade: '))

peso = float(input('Insira o seu peso: '))

gravidez = input('Você esta em periodo de gravidez? (S = Sim/ N= Não): ').lower()

doar = input('Você fez doação em um periodo de 90 dias? (S = Sim/ N= Não): ').lower()

if idade >= 16 and idade <= 69 and gravidez == 'n' and doar == 'n' and peso >= 50:
    print('Você pode doar sangue!!!')
else:
    print('Você não pode doar sangue.')