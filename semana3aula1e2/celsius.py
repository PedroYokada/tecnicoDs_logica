celsius = float(input("Insira a temperatura em Celsius: "))

calculo = input("Insira 'f' para Fahrenheit ou 'k' para Kelvin: ").lower()

if calculo == 'f':
    f = (celsius * 9/5) + 32
    print(f"Resultado: {f:.2f} °F")  
elif calculo == 'k':
    k = celsius + 273.15  
    print(f"Resultado: {k:.2f} K") 
else:
    print("Operação inválida!")

