import random  # Importa o módulo para gerar escolhas aleatórias

def jogar():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Escolha uma das opções: ")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    try:
        escolha_jogador = int(input("Digite o número da sua escolha: "))
        if escolha_jogador not in [1, 2, 3]:
            print("Escolha inválida! Tente novamente.")
            return

        escolha_computador = random.randint(1, 3)

        print(f"Você escolheu: {opcoes[escolha_jogador]}")
        print(f"O computador escolheu: {opcoes[escolha_computador]}")

        # Regras do jogo
        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif (escolha_jogador == 1 and escolha_computador == 3) or \
             (escolha_jogador == 2 and escolha_computador == 1) or \
             (escolha_jogador == 3 and escolha_computador == 2):
            print("Você venceu!")
        else:
            print("Você perdeu!")

    except ValueError:
        print("Por favor, digite um número válido.")

# Inicia o jogo
jogar()