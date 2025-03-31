sistemas = {
    'r': 'Sistema Respiratório: Realiza trocas gasosas.',
    'c': 'Sistema Circulatório: Transporta nutrientes e oxigênio.',
    'd': 'Sistema Digestório: Processa alimentos e absorve nutrientes.',
    'n': 'Sistema Nervoso: Controla respostas e processos do corpo.'
}

sistema = input('Insira a letra correspondente ao sistema humano desejado: ').lower()

if sistema in sistemas:
    print(sistemas[sistema])
else:
    print('Sistema inválido!')

# https://www-w3schools-com.translate.goog/python/python_dictionaries.asp?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc
