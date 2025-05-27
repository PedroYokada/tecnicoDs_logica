distancia = float(input("Digite a distância da viagem em km: "))
orcamento = float(input("Digite o seu orçamento em R$: "))
prioriza_rapidez = input("Você prioriza rapidez? (sim/não): ").lower() == "sim"

if distancia > 1000:
    if prioriza_rapidez:
        meio_transporte = "Avião"
    else:
        meio_transporte = "Ônibus" if orcamento < 300 else "Avião"
elif distancia > 300:
    if orcamento < 100:
        meio_transporte = "Ônibus"
    else:
        meio_transporte = "Carro" if prioriza_rapidez else "Trem"
else:
    meio_transporte = "Carro" if orcamento >= 50 else "Bicicleta"

print(f"Recomendamos utilizar: {meio_transporte}")
