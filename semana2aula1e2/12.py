def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
        case _:
            return "Valor {} inválido".format(dia)

numero_dia = int(input('Informe o número do dia da semana (1 a 7): '))

print(dia_semana(numero_dia))