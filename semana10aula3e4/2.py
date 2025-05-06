# Inicializa a variável 'tabuada' com 1
tabuada = 1

# Loop externo: controla de qual número será exibida a tabuada (de 1 a 5)
while tabuada <= 5:
    # Inicializa o 'numero' a ser multiplicado com a 'tabuada'
    numero = 1
    
    # Exibe o título da tabuada atual
    print(f"Tabuada do {tabuada}:")
    
    # Loop interno: realiza as multiplicações da tabuada de 1 até 10
    while numero <= 10:
        # Exibe o resultado da multiplicação atual
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        # Incrementa o número para a próxima multiplicação
        numero += 1

    # Linha em branco para separar visualmente as tabuadas
    print("\n")
    
    # Incrementa a tabuada para gerar a próxima
    tabuada += 1
