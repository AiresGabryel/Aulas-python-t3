'''Primeiro Exercício: Soma de elementos pares 
Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os elementos pares contidos nela. 
Exemplo: [2,4,10,3,9,7,15,22] 
Saída: A soma dos pares é: x 
'''

def somar_pares(Lista_de_numeros):
    resultado = 0
    for numero in Lista_de_numeros:
        if numero % 2 == 0: #Verifica se é par
            resultado += numero # resultado = resultado + numero
    return resultado

lista = [1,4,10,6,3,7,9]

print(f'A soma dos pares na lista é: {somar_pares(lista)}')