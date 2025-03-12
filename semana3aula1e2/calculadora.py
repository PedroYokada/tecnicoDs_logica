def calculadora(num1, num2, op):
    match op:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            return num1 / num2 if num2 != 0 else "Erro: divisão por zero!"
        case _:
            return "Operação inválida!"

# Entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = int(input("Escolha a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

# Chamada e exibição do resultado
resultado = calculadora(num1, num2, op)
print(f"Resultado: {resultado}")