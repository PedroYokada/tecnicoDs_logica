valores = []
quadrados = []

for i in range(10):
  numero = float(input(f'Insira o {i+1}º número: '))
  valores.append(numero)
  quadrados.append(numero ** 2)

print(valores)
print(quadrados)