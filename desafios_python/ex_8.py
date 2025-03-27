'''Oitavo Exercício: Verificador de Palíndromos
Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
pode ser lida da mesma forma de trás para frente) e False caso contrário.
Exemplo:
entrada = "radar"
Saída: True'''

def eh_palindromo(palavra):
    # Removendo espaços e transforma em minúsculas para evitar diferenciação
    palavra = palavra.replace(" ", "").lower()
    # Verificando se a palavra é igual à sua inversa
    return palavra == palavra[::-1]

# Teste
palavra = input("Digite uma palavra: ")
print("É um palíndromo?", eh_palindromo(palavra))
