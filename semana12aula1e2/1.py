num = int(input("Digite um número: "))
if num > 0:
    if num % 2 == 0:
        print("O número é positivo e par.")
    else:
        print("O número é positivo e ímpar.")
elif num < 0:
    if num % 2 == 0:
        print("O número é negativo e par.")
    else:
        print("O número é negativo e ímpar.")
else:
    print("O número é zero.")
