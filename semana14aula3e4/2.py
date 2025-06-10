# Lista com os dados de 3 empresas
# Cada número é o resultado de um projeto
dados = [[75, 90, 60],  # Empresa 0
         [65, 70, 85],  # Empresa 1
         [80, 55, 75]]  # Empresa 2

# Calcula a média de cada projeto (coluna)
for i in range(len(dados[0])):  # Para cada projeto (0, 1, 2)
    soma = 0
    for empresa in dados:  # Para cada empresa
        soma += empresa[i]  # Soma o valor do projeto
    media = soma / len(dados)  # Calcula a média
    print(f"Média do Projeto {i}: {media}")

# Descobre qual foi o melhor projeto de cada empresa (linha)
for i, empresa in enumerate(dados):  # Para cada empresa
    projeto_mais_bem_sucedido = max(empresa)  # Pega o maior valor
    print(f"Empresa {i} - Projeto Mais Bem-Sucedido: {projeto_mais_bem_sucedido}")
