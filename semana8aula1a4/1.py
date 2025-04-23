idade = int(input('Qual a idade: '))

exame = input('Você possui exame médico? (S = SIM/ N = NÃO): ').lower()

infracao = input('Você cometeu uma infração de transito? (S = SIM/ N = NÃO): ').lower()

if idade >= 18 and exame == 's' and infracao == 'n':
    print('Conseguiu pegar a CNH!!!')
else:
    print('Não pegou CNH!')