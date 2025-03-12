fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))

calculo = input("Insira 'c' para Celsius ou 'k' para Kelvin: ").lower()

if calculo == 'c':
    c = (fahrenheit - 32) * 5/9  
    print(f"Resultado: {c:.2f} °C")
elif calculo == 'k':
    k = (fahrenheit - 32) * 5/9 + 273.15  
    print(f"Resultado: {k:.2f} K")
else:
    print("Operação inválida!")
