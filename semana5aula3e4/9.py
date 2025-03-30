livro_qntd = int(input("Digite a quantidade de livros que você vai comprar: "))

valor = float(input("Digite o preço de cada livro: "))

valor_compra = float(livro_qntd * valor)

if livro_qntd == 0 or livro_qntd == 1:
  print("Não tem desconto.")
  valor_final = valor_compra
  desconto_livros = 0
elif livro_qntd == 2 or livro_qntd == 3:
  desconto_livros = valor_compra * 0.1
  valor_final = valor_compra - desconto_livros
elif livro_qntd == 4 or livro_qntd == 5:
  desconto_livros = valor_compra * 0.2
  valor_final = valor_compra - desconto_livros
else:
  desconto_livros = valor_compra * 0.3
  valor_final = valor_compra - desconto_livros
  
print(f"O valor total da compra sem desconto é de: {valor_compra:.2f}R$")
print(f"O valor com desconto é de:: {desconto_livros:.2f}R$")
print(f"O valor final da compra é de: {valor_final:.2f}R$")