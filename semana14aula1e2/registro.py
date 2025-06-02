from collections import Counter  # Importa o Counter para contar itens facilmente
from datetime import datetime    # Importa datetime para manipular datas

# Lista de dicionários com as vendas (produto, quantidade e data)
vendas = [
    {"produto": "Teclado", "quantidade": 10, "data": "2021-03-15"},
    {"produto": "Mouse", "quantidade": 15, "data": "2021-03-17"},
    {"produto": "Monitor", "quantidade": 7, "data": "2021-04-01"},
    # ... outros dados podem ser adicionados aqui ...
]

# Cria um contador para contar quantas unidades foram vendidas de cada produto
contador_produtos = Counter()
for venda in vendas:
    # Soma a quantidade vendida do produto atual
    contador_produtos[venda["produto"]] += venda["quantidade"]

# Seleciona os 5 produtos mais vendidos
cinco_mais_vendidos = contador_produtos.most_common(5)

# Cria um contador para somar vendas agrupadas por mês
vendas_por_mes = Counter()
for venda in vendas:
    # Converte a data (string) em objeto datetime e formata para "YYYY-MM"
    mes = datetime.strptime(venda["data"], "%Y-%m-%d").strftime("%Y-%m")
    # Soma a quantidade vendida naquele mês
    vendas_por_mes[mes] += venda["quantidade"]

# Ordena os meses do maior para o menor em quantidade de vendas
meses_maior_venda = vendas_por_mes.most_common()

# Exibe os resultados
print("Cinco produtos mais vendidos:", cinco_mais_vendidos)
print("Vendas por mês:", meses_maior_venda)