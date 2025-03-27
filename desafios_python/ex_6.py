def combinar_dict(d1: dict, d2: dict):
    novo_dicionario = {}

    for chaves, valor in d1.items():
        novo_dicionario[chaves] = valor

    for chave, valor in d2.items:
        if chave in novo_dicionario.keys():
            novo_dicionario[chaves] += valor
        else:
            novo_dicionario[chave] = valor

    return novo_dicionario

 #TAFERA -> CONSERTAR A LÓGICA 
print(f'Novo dicionário: {combinar_dict(d1, d2)}')