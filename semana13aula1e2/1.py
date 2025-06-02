num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

operacao = int(input('1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão: '))

if operacao == 1:
    resultado = num1 + num2
    print(f'Resultado: {resultado:.2f}')
elif operacao == 2:
    resultado = num1 - num2
    print(f'Resultado: {resultado:.2f}')
elif operacao == 3:
    resultado = num1 * num2
    print(f'Resultado: {resultado:.2f}')
elif operacao == 4:
    if num2 == 0:
        print('Não pode dividir por zero!')
    else:
        resultado = num1 / num2
        print(f'Resultado: {resultado:.2f}')
else:
    print('Operação inválida.')
