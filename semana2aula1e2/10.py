# calculando o valor de uma area de um triangulo retangulo

import math

cateto1 = float(input('Insira o valor do cateto 1: '))

cateto2 = float(input('Insira o valor do cateto 2: '))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f'HIPOTENUSA =  {hipotenusa:.4f}')

