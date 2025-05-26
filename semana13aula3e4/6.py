def exemplo_pattern_matching(valor):
    match valor:
        case 'A':
            return "Opção A"
        case 'B':
            return "Opção B"
        case _:
            return "Outra opção"

print(exemplo_pattern_matching('A'))  
# Saída: Opção A
