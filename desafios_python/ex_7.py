lista_numeros = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,9,9,9]


def pesquisar_numeros_frequentes(lista_numeros: list):

#FUncção que recebe a lista d numeros
    frequencia = {}
    
    #percorrendo a lista de numeros
    for numero in lista_numeros:
        # o numero é uma chave existentno meu dicionario ?
        if numero in frequencia:
            #se sim, adicione um numero no valor
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
            #se não, diga que é a primeira vez
            

    numeros_ordenados = sorted(  frequencia.keys(), key=lambda chave: (frequencia[chave], chave), reverse=True)

    return numeros_ordenados[:3]


print(lista_numeros)