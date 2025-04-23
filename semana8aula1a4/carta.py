idade = int(input('Insira a sua idade: '))

exame = True

infracao = input('Você cometeu alguma infração de transito?(S = Sim/ N= Não)').upper()

if idade >= 18 and exame == True and infracao == 'N':
    print('Você pode retirar a sua CNH!!!')
else:
    print('Você não pode retirar a sua CNH.')