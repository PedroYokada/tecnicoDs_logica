renda = float(input('Qual a sua renda mensal?: '))

score = float(input('Qual o seu score?: '))

fiador = input('Possui um fiador que tenha um score maior ou igual a 700?(S = Sim/ N= Não): ').lower()

if (renda >= 2000 and score >= 600) or fiador == 's':
    print('Cliente é elegível para um empréstimo!!!')
else:
    print('Cliente não elegível para um empréstimo.')
