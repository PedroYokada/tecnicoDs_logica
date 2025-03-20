import math

a = float(input("Insira o valor de a: "))

if a == 0:
    print("a equação não é do segundo grau!")
else:
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))
    
    delta = b**2 - (4*a*c)
    
    if delta < 0:
        print("a equação não possui raizes reais.")
    elif delta == 0:
        r = -b / (2*a)
        print(f"a equação possui apenas uma raiz real, a raiz é: {r:.2f}")
    else:
        x1 = (-b +  math.sqrt(delta))/(2*a)
        x2 = (-b -  math.sqrt(delta))/(2*a)
        print(f"Delta é positivo, portanto a equação possui duas raiz reais, x1 = {x1:.2f} e x2 = {x2:.2f} ")