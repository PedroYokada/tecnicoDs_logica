idade = int(input('Insira a sua idade: '))

if idade >= 18:
    print('Entrada permitida!!!')

elif idade >= 15 and idade <= 17:
    permissao = input('Você tem autorização dos pais ou está acompanhado de um adulto? (S/N) ').upper()

    autorizacao = input('Você tem autorização dos pais ou vai entrar acompanhado de um adulto? (S = Sim/ N= Não): ').lower()

    if permissao == 'S' or autorizacao == 'S':
        print('Entrada permitida! (Autorização/acompanhante válido)')
    else:
        print('Entrada negada. (Menor de 18 anos sem autorização/acompanhante)')
else: 
    print('Entrada negada. Menor de 15 anos não permitido!')




