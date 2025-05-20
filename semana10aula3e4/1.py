# import pdb

x = "global"  # Variável global

# Loop for para iterar duas vezes
for i in range(2):
    # import pdb; pdb.set_trace()
    if i == 0:
        y = "local na primeira iteração"  # 'y' definida no bloco if
    else:
        y = "local na segunda iteração"  # 'y' redefinida no bloco else

    
    print(f"Iteração {i+1}:")
    print(f"x: {x}")  # 'x' é global, acessível de qualquer lugar
    print(f"y: {y}")  # 'y' é acessível aqui porque foi definida em todos os caminhos possíveis
