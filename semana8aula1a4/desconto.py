best = input('O livro é um Best-Seller? (S = Sim/ N= Não)').upper()
lancamento = input('O livro foi lançado a mais de dois anos? (S = Sim/ N= Não)').upper()
qntd = int(input('Qual a quantidade de livros que você deseja comprar? :'))
preco_unidade = float(input('Qual o valor unitário do livro? :'))

valor_compra = preco_unidade * qntd


if best == 'S' or lancamento == 'S':
    valor_compra = valor_compra * 0.8
if qntd > 3:
    valor_compra = valor_compra * 0.75
    
    
print(f'O valor da compra é de: R${valor_compra:.2f}')