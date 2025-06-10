vetor = []

for i in range(7):
  numero = float(input(f"Insira o {i}º numero: "))
  vetor.append(numero)
  
x = int(input(f"Insira o valor X: "))
y = int(input(f"Insira o valor X: "))

if 0 <= x < 8 and 0 <= y < 8:
    soma = vetor[x] + vetor[y]
    print(f"\nSoma dos valores nas posições {x} e {y}: {soma}")
else:
    print("\nErro: posições X e Y devem estar entre 0 e 7.")