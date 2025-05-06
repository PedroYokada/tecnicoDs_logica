elementos_quimicos = {
    'Li': {"Nome": "Lítio", "Massa": "6,941", "Número Atômico": "3"},
    'Na': {"Nome": "Sódio", "Massa": "22,990", "Número Atômico": "11"},
    'K':  {"Nome": "Potássio", "Massa": "39,098", "Número Atômico": "19"},
}

desejo = 'S'

while desejo != 'N':
    sigla = input("Digite a sigla do elemento químico: ").capitalize()
    elemento = elementos_quimicos.get(sigla)

    if elemento:
        print("Nome:", elemento["Nome"])
        print("Número Atômico:", elemento["Número Atômico"])
        print("Massa:", elemento["Massa"])
    else:
        print("Elemento químico não encontrado.")
        
    desejo = input('Deseja executar o código novamente? S/N: ').strip().upper()


    

    