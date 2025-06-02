while True:
    operacao = int(input('\n1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Resto, 6-Encerrar: '))

    if operacao == 6:
        print('Encerrando...')
        break

    if operacao not in [1, 2, 3, 4, 5]:
        print('Operação inválida.')
        continue

    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))

    if operacao == 1:
        num3 = num1 + num2
    elif operacao == 2:
        num3 = num1 - num2
    elif operacao == 3:
        num3 = num1 * num2
    elif operacao == 4:
        if num2 == 0:
            print('Não pode dividir por zero!')
            continue
        num3 = num1 / num2
    elif operacao == 5:
        if num2 == 0:
            print('Não pode dividir por zero!')
            continue
        num3 = num1 % num2

    print(f'O resultado da operação é: {num3:.2f}')


   

