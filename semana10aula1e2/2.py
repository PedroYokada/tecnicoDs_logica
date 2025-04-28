import random

numero_secreto = random.randint(1, 50)
tentativas = 0
limite_tentativas = 5

while tentativas < limite_tentativas:
    palpite = int(input(f"Tentativa {tentativas + 1}/{limite_tentativas}. Adivinhe o número entre 1 e 50: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

    if tentativas == limite_tentativas:
        print(f"Você atingiu o limite de tentativas. O número secreto era {numero_secreto}.")
        break
