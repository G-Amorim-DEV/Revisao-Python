""" Exercício 03
Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade
de vezes que essa vogal aparece no texto.
A função deve receber o texto como entrada e retornar o dicionário.
Exemplo:
Para o texto abaixo:
texto = ' faculdade impacta de tecnologia'
A função deve devolver o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 } """

def contar_vogais(texto):
    vogais = "aeiou"
    resultado = {}

    texto = texto.lower()

    for v in vogais:
        quantidade = texto.count(v)  
        if quantidade > 0:
            resultado[v] = quantidade

    return resultado



texto = input("Digite o texto para contar quantas vogais contém nesse texto: ")
print(contar_vogais(texto))




