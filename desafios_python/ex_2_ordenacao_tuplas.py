'''Segundo Exercício: Ordenação de Tuplas

Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade, escreva uma função que retorne a lista ordenada pela idade de forma crescente.

Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”) 
Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”) '''


def ordenar_tuplas(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key= lambda tupla: tupla[1])
    return lista_ordenada

lista = [('Samuel', 23), ('Karynne', 20), ('Carol', 22), ('Kleber', 24), ('Vinicius', 21)]

print(f'As tuplas ordenadas por idade: {ordenar_tuplas(lista)}')