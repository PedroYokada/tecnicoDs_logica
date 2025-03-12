kelvin = float(input("Insira a temperatura em Kelvin: "))

calculo = input("Insira 'c' para Celsius ou 'f' para Fahrenheit: ").lower()

if calculo == 'c':
    c = kelvin - 273.15 
    print(f"Resultado: {c:.2f} °C")
elif calculo == 'f':
    f = (kelvin - 273.15) * 9/5 + 32  
    print(f"Resultado: {f:.2f} °F")
else:
    print("Operação inválida!")
