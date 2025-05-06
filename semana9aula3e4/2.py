import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 1000)
    tentativas = 0
    palpite = 0
    
    while palpite != numero_secreto:
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Mais alto!")
        elif palpite > numero_secreto:
            print("Mais baixo!")

    print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

jogo_adivinhacao()
