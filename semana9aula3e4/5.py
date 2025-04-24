alfabeto = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
}

letra = input("Digite uma letra: ").lower()

if letra in alfabeto:
    print(f'A letra "{letra}" é reconhecida do alfabeto.')
else:
    print("Isso não é uma letra do alfabeto.")
