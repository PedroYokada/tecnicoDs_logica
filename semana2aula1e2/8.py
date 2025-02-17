# Suponha que estes sejam os valores corretos para login e senha
login_correto = "usuario123"
senha_correta = "senha123"
# Função para verificar o acesso
def verificar_acesso(login, senha):
    if login == login_correto and senha == senha_correta:
        return "Acesso permitido"  
    else:
        return "Acesso negado"

