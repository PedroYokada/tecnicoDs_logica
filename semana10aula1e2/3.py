# Início de um laço infinito: ele continuará executando até recebermos uma senha válida
while True:
    # Solicita ao usuário que crie uma senha, mostrando as regras necessárias
    senha = input("Crie uma senha (deve ter pelo menos 8 caracteres e conter números e letras): ")
    
    # Verifica se a senha atende a três critérios:
    # 1. Ter pelo menos 8 caracteres
    # 2. Conter pelo menos um número
    # 3. Conter pelo menos uma letra
    if len(senha) >= 8 and any(char.isdigit() for char in senha) and any(char.isalpha() for char in senha):
        # Se a senha for válida, informa o sucesso
        print("Senha criada com sucesso!")
        # Encerra o laço, pois a senha válida já foi criada
        break
    else:
        # Se a senha não atender aos critérios, informa o erro e repete o laço
        print("A senha não atende aos critérios, tente novamente.")
