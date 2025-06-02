# Jogo da Velha simples no terminal

def exibir_tabuleiro(tabuleiro):
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    for combo in combinacoes:
        if all(tabuleiro[i] == jogador for i in combo):
            return True
    return False

def jogo_da_velha():
    tabuleiro = [" " for _ in range(9)]
    jogador_atual = "X"
    
    while True:
        exibir_tabuleiro(tabuleiro)
        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[jogada] != " " or jogada not in range(9):
                print("Posição inválida. Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Digite um número de 1 a 9.")
            continue

        tabuleiro[jogada] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if " " not in tabuleiro:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if _name_ == "_main_":
    jogo_da_velha()