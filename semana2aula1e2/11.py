pct_bateria = int(input('Insira a porcentagem da bateria do seu celular: '))

if pct_bateria == 100:
    print('A bateria do seu celular está cheia!')
elif 70 <= pct_bateria <= 99:
    print('A bateria do seu celular está com carga alta!')
elif 40 <= pct_bateria <= 69:
    print('A bateria do seu celular está com uma carga mediana!')
elif 16 <= pct_bateria <= 39:
    print('A bateria do seu celular está com uma carga baixa!')
elif 0 <= pct_bateria <= 15:
    print('A bateria do seu celular está com carga muito baixa!')
else:
    print('Valor da carga inválido')


