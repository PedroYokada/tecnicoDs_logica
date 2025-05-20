import random

palavras = ["PYTHON", "JOGO", "CODIGO"]
tamanho = 10

def criar_grade():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [[random.choice(letras) for _ in range(tamanho)] for _ in range(tamanho)]

def inserir(grade):
    for p in palavras:
        l, c = random.randint(0, tamanho-1), random.randint(0, tamanho-len(p))
        for i in range(len(p)):
            grade[l][c+i] = p[i]

def mostrar(grade):
    for linha in grade:
        print(" ".join(linha))

def jogar():
    grade = criar_grade()
    inserir(grade)
    mostrar(grade)

    achadas = []
    while len(achadas) < len(palavras):
        pal = input("\nAdivinhe uma palavra: ").upper()
        if pal in palavras and pal not in achadas:
            achadas.append(pal)
            print("✅ Correto!")
        else:
            print("❌ Tente novamente.")

    print("\n🎉 Você encontrou todas!")

jogar()
