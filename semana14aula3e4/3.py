def somar(a, b):
    return a + b

# Exemplo de uso de um laço FOR com range
total = 0
for i in range(4): # Isso vai iterar i de 0 a 3
    total = somar(total, i)

print(total)
