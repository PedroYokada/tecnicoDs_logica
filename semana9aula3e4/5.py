
letra = input("Digite uma letra: ").lower()


if letra in ('a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z'):
    print(f"A letra '{letra}' está no alfabeto.")
else:
    print(f"A letra '{letra}' NÃO está no alfabeto.")
