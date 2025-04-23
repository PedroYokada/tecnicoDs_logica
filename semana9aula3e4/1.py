# Dicionário com informações dos elementos químicos
elementos_quimicos = {
    "H": {"Nome": "Hidrogênio", "Número Atômico": 1, "Massa": 1.008},
    "He": {"Nome": "Hélio", "Número Atômico": 2, "Massa": 4.0026},
    "Li": {"Nome": "Lítio", "Número Atômico": 3, "Massa": 6.94},
    # Adicione mais elementos aqui
}

# Função para exibir informações do elemento químico
def exibir_informacoes_elemento(sigla):
    elemento = elementos_quimicos.get(sigla)
    if elemento:
        for chave, valor in elemento.items():
            print(f"{chave}: {valor}")
    else:
        print("Elemento químico não encontrado.")

# Leitura da sigla do elemento químico
sigla_elemento = input("Digite a sigla do elemento químico: ").title()
exibir_informacoes_elemento(sigla_elemento)
