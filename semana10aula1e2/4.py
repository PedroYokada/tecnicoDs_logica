# Define a palavra que o jogador deve adivinhar
palavra_secreta = "misterio"

# Cria uma lista com "_" para cada letra da palavra secreta, representando as letras não adivinhadas
letras_acertadas = ['_' for _ in palavra_secreta]

# Inicializa a variável de erros como 0 (o jogador começa sem erros)
erros = 0

# Início do laço: continua enquanto o jogador tiver menos de 3 erros e ainda houver "_" (letras não adivinhadas)
while erros < 3 and '_' in letras_acertadas:
    # Pede para o jogador digitar uma letra e converte para minúscula
    palpite = input("Digite uma letra: ").lower()

    # Verifica se o palpite está na palavra secreta
    if palpite in palavra_secreta:
        # Se sim, percorre a palavra secreta
        for i, letra in enumerate(palavra_secreta):
            # Se a letra da palavra for igual ao palpite, atualiza a posição correspondente na lista de letras acertadas
            if letra == palpite:
                letras_acertadas[i] = palpite
    else:
        # Se o palpite não estiver na palavra, incrementa o número de erros
        erros += 1
        # Informa ao jogador quantas tentativas restam
        print(f"Erro! Você tem {3 - erros} tentativas restantes.")

    # Exibe a situação atual da palavra (letras acertadas e espaços ainda escondidos)
    print(" ".join(letras_acertadas))

# Quando o laço terminar, verifica se o jogador ganhou ou perdeu
if '_' not in letras_acertadas:
    # Se não houver mais "_" na lista, o jogador acertou a palavra
    print("Parabéns, você adivinhou a palavra!")
else:
    # Caso contrário, o jogador perdeu
    print(f"Você perdeu. A palavra era: {palavra_secreta}.")

