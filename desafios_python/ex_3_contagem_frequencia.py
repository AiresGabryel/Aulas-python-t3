'''Terceiro Exercício: Contagem de Frequência 

Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os caracteres da string e os valores representam quantas vezes cada caractere aparece. '''

#Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’] 

def conta_frequencia(palavras):
    lista = palavras.split(' ')

    dicionario = {}

    for palavra in lista:
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra)
    return dicionario

linguagens = 'Java Java Java Javascript Python Ruby Ruby Cobol Javascript Java Java League_of_Legends'

print('Quantidade de frequencia')
print('-'*100)
print(conta_frequencia(linguagens))