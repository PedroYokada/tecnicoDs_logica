# Inicia a partir de 1500 e incrementa de 5 em 5, pois estamos
# procurando um número divisível por 5.
# Isso reduz o número de iterações necessárias.
for numero in range(1500, 2701, 5):
    if numero % 7 == 0:
        print(f"O primeiro número divisível por 5 e 7 entre 1500 e 2700 é: {numero}")
        break
