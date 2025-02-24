habilitacao = input('Tem habilitação ? (s = Sim/n = Não)').lower()

if habilitacao == 's':
    habilitacao = True
else:
    habilitacao = False

# == operador de comparação, = operador de atribuição

idade = int(input('Digite a sua idade: '))

if idade >= 18 and habilitacao == True:
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")


