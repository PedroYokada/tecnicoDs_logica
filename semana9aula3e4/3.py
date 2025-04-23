def classificar_idade():
    idade = int(input("Digite sua idade: "))
    
    if idade <= 12:
        categoria = "Criança"
    elif idade <= 17:
        categoria = "Adolescente"
    elif idade <= 64:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    print(f"Você está na categoria: {categoria}")

classificar_idade()
