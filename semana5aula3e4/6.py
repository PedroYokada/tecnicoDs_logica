import time

# Lista com números de 0 a 999999
lista = list(range(1000000))

start_time = time.time()  # Tempo inicial

# Criando listas separadas para pares e ímpares
pares = [x for x in lista if x % 2 == 0]
impares = [x for x in lista if x % 2 != 0]

end_time = time.time()  # Tempo final

print(f"Tempo de execução: {end_time - start_time} segundos.")
# Exibir os primeiros elementos para ver o resultado
print("Exemplo de números pares:", pares[:10])
print("Exemplo de números ímpares:", impares[:10])