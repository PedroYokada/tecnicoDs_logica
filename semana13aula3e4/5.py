def opcao_a():
    return "Opção A executada"

def opcao_b():
    return "Opção B executada"

switch_dict = {
    'A': opcao_a,
    'B': opcao_b
}

valor = 'A'
print(switch_dict.get(valor, lambda: "Opção inválida")())  
# Saída: Opção A executada
