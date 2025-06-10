import random
import time
import os

# Cores e sons simulados
stimuli = {
    'R': {'name': 'Vermelho', 'sound': 'Beep!'},
    'G': {'name': 'Verde', 'sound': 'Ding!'},
    'B': {'name': 'Azul', 'sound': 'Boop!'},
    'Y': {'name': 'Amarelo', 'sound': 'Dong!'}
}

# Limpa a tela (para Windows e Unix)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Mostra a sequência com atraso entre os estímulos
def show_sequence(sequence):
    clear_screen()
    print(">>> Memorize a sequência:")
    for s in sequence:
        print(f"{stimuli[s]['name']} - {stimuli[s]['sound']}")
        time.sleep(1)
        clear_screen()
        time.sleep(0.4)
    print(">>> Agora é sua vez!")

# Recebe entrada do usuário
def get_player_input(length):
    while True:
        entrada = input(f"Digite a sequência ({length} letras - R, G, B, Y): ").upper()
        if len(entrada) == length and all(c in stimuli for c in entrada):
            return list(entrada)
        print("Entrada inválida. Tente novamente.")

# Função principal do jogo
def jogar():
    sequence = []
    score = 0
    print("=== Bem-vindo ao Memória Sensorial ===")
    print("Repita as sequências usando as letras:")
    print("R = Vermelho | G = Verde | B = Azul | Y = Amarelo")
    input("Pressione ENTER para começar...")

    while True:
        next_color = random.choice(list(stimuli.keys()))
        sequence.append(next_color)
        show_sequence(sequence)
        resposta = get_player_input(len(sequence))

        if resposta == sequence:
            score += 1
            print(">>> Correto! Próxima rodada...")
            time.sleep(1)
        else:
            print(">>> Você errou!")
            print(f"Pontuação final: {score}")
            break

if _name_ == "_main_":
    jogar()