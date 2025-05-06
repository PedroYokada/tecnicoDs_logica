# Solicita ao usuário o valor que deseja sacar
valor_saque = int(input("Digite o valor do saque: "))

# Lista das notas disponíveis no caixa, em ordem decrescente
notas = [50, 20, 10, 5]

# Dicionário para armazenar a quantidade de cada nota usada
quantidade_notas = {}

# Loop para calcular quantas notas de cada valor serão usadas
for nota in notas:
    # divmod retorna o quociente (quantas notas cabem) e o resto (valor que sobra)
    quantidade_notas[nota], valor_saque = divmod(valor_saque, nota)

# Exibe o resultado
print("Quantidade de notas para o saque:")

# Percorre o dicionário e exibe apenas as notas utilizadas
for nota, quantidade in quantidade_notas.items():
    if quantidade > 0:
        print(f"Notas de R${nota}: {quantidade}")
