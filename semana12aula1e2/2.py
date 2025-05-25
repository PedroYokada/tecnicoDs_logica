tipo_produto = input("Insira o tipo de produto (tecnologia/vestuario): ")
quantidade = int(input("Insira a quantidade de produtos: "))
if tipo_produto == "tecnologia":
    if quantidade > 2:
        print("Você ganhou um desconto de 10%!")
    else:
        print("Infelizmente, você não atingiu a quantidade necessária para um desconto.")
elif tipo_produto == "vestuario":
    if quantidade > 3:
        print("Você ganhou um desconto de 20%!")
    else:
        print("Infelizmente, você não atingiu a quantidade necessária para um desconto.")
else:
    print("Tipo de produto não reconhecido.")
