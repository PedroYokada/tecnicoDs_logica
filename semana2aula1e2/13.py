tabuada = int(input("Escolha um numero para o calculo da tabuada: "))

cont = 0

print(f'Tabuada do numero: {tabuada}')

for i in range(0,11):
    print(f'{tabuada} X {cont} = {tabuada * cont}')
    cont += 1