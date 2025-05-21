# Leitura das entradas do usuário
conectado = input("O usuário está conectado (sim/não)? ").lower()
amigo = input("O destinatário é um amigo (sim/não)? ").lower()

# Verificação das condições e exibição da mensagem correspondente
if conectado == "sim" and amigo == "sim":
    print("Mensagem enviada")
else:
    print("Mensagem não enviada")
