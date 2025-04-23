def consulta_candidato():

    numero = int(input('Digite o número do candidato (1 ou 2): '))
    
    if numero == 1:
        print('\nInformações do Candidato 1:')
        print('Nome: Candidato A')
        print('Partido: Partido X')
        print('Propostas: Saúde e Educação')
    elif numero == 2:
        print('\nInformações do Candidato 2:')
        print('Nome: Candidato B')
        print('Partido: Partido Y')
        print('Propostas: Segurança e Infraestrutura')
    else:
        print('Candidato não encontrado. Por favor, digite 1 ou 2.')


consulta_candidato()
