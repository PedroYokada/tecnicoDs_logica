portfolio = input('Você possui um bom portifólio? (S = Sim/ N= Não): ').lower()

audicao = input('Você possui uma boa audição? (S = Sim/ N= Não): ').lower()

treinamento = int(input('Quanto tempo de treinamento prévio você possui?: '))

if (portfolio == 's') or (audicao == 's' and treinamento >= 2):
    print('Candidato será admitido!!!')
else:
    print('Candidato não admitido.')
