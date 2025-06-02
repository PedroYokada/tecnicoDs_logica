import os
import random
logo = 'Jogo de Adivinhação'
print(f'{logo: ^10}')

decisao = input('Deseja jogar o modo aleatório ou personalizado?').lower()
palavra_aleatoria = ['perfume', 'beterraba', 'melancia', 'escola']
letras_acertadas = ''
numero_tentativas = 0

if decisao == 'aleatório':
    palavra_aleatoria_esco = random.choice(palavra_aleatoria)
    while True:
        
            letra_digitada = input('Digite uma letra: ')
            numero_tentativas += 1
            os.system('cls')
            if len(letra_digitada) > 1:
                print('Digite apenas uma letra.')
                continue

            if letra_digitada in palavra_aleatoria_esco:
                letras_acertadas += letra_digitada

            palavra_formada = ''
            for letra_secreta in palavra_aleatoria_esco:
                if letra_secreta in letras_acertadas:
                    palavra_formada += letra_secreta
                else:
                    palavra_formada += '*'

            print('Palavra formada:', palavra_formada)

            if palavra_formada == palavra_aleatoria_esco:
                os.system('cls')
                print('VOCÊ GANHOU!! PARABÉNS!')
                print('A palavra era', palavra_aleatoria_esco)
                print('Tentativas:', numero_tentativas)
                
                letras_acertadas = ''
                numero_tentativas = 0

elif decisao == 'personalizado':

    personalizado = input('Insira uma palavra: ')

    while True:
        letra_digitada = input('Digite uma letra: ')
        numero_tentativas += 1

        if len(letra_digitada) > 1:
            print('Digite apenas uma letra.')
            continue

        if letra_digitada in personalizado:
            letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in personalizado:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print('Palavra formada:', palavra_formada)

        if palavra_formada == personalizado:
            os.system('cls')
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', personalizado)
            print('Tentativas:', numero_tentativas)
            
            letras_acertadas = ''
            numero_tentativas = 0

else:
    print('Insira as opções corretamente')