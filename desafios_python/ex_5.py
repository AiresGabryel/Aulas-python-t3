notas =  {'Silvano': [10,10,10], 'Gabriel': [10,10,10], 'Joyce':[2,3,8.5]}

def calcular_medias(notas: dict):
    lista_medias = []

    for chaves, valor in notas.items():
        media = round (sum(valor) / len(valor), 2)
        lista_medias.append( (chaves, media) )

    return lista_medias 
    
print(calcular_medias(notas))


dicionario1 = {'A': 1}
dicionario2 = {'A': 2}


