""" Exercício 01
Preencha um dicionário com as informações de 5 produtos fornecidos pelo usuário.
- Solicite os dados ao usuário
- Utilize o nome do produto como chave e o preço como valor.
- Percorra o dicionário e exiba o nome dos produtos com preço
superior a R$ 50,00.
Exemplo:
{'caneta': 3.0, 'Pen drive': 100.0,'Teclado': 30.0, 'Lápis': 1.5}
"""

catalogo = {}

continuacao = True

while continuacao:
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o preço do produto: "))

    catalogo[produto] = valor

    continuar = input("Digite se deseja adicionar mais produtos y(yes) ou n(no): ").lower()

    if continuar in ["y", "yes"]:
        continuacao = True
    else:
        continuacao = False

print("\nProdutos com valores superiores a R$50,00:")
for produto, valor in catalogo.items():
    if valor > 50:
        print(f"{produto}: R$ {valor:.2f}")

print("\nCatálogo completo:")
for produto, valor in catalogo.items():
    print(f"{produto}: R$ {valor:.2f}")
