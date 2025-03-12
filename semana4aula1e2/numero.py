def nome_funcao(num):
    match num:
        case 1:
            return 'Numero 1'
        case 2:
            return 'Numero 2'
        case 3:
            return 'Numero 3'
        case 4:
            return 'Numero 4'
        case _:
            return "Numero inválido"

num = int(input("Escolha um número: "))

print(nome_funcao(num))  
