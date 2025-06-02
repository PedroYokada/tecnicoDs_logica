import random #importa a biblioteca

def jogo_pedra_papel_tesoura():
    escolhas = ["pedra", "papel", "tesoura"] #define as opções do jogador
    computador = random.choice(escolhas) #o computador escolhe uma opção aleatória
    jogador = input("Escolha pedra, papel ou tesoura: ").lower() #pede a escolha do jogador e muda para minúsculas

    if jogador not in escolhas: #verifica se a escolha do jogador é válida
        print("Escolha inválida! Tente novamente.") #mostra a mensagem de erro
        return #sai da função se a escolha for inválida

    print(f"\nO computador escolheu: {computador}") #mostra a escolha do computador
   
    if jogador == computador: #se as escolhas forem iguais, mostra que foi empate
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"): #checa se o jogador venceu
        print("Você ganhou!")
    else: #se não empatou e o jogador não venceu, mostra que o jogador perdeu
        print("Você perdeu!")

jogo_pedra_papel_tesoura() #chama a função para iniciar o jogo