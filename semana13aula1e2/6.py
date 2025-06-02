num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

operacao = ("+,-,*,/,%: ")

match operacao:
    case "+":
        num3 = num1 + num2
    case "-":
        num3 = num1 - num2
    case "*":
        num3 = num1 * num2
    case "/":
        if num2 != 0:
             num3 = num1 / num2
        else:
           print("Valor incorreto!")
    case "%":
         num3 = num1 % num2
    case _:
        print("Operacao inválida")

print(f"o valor final é {num3:.2f}")