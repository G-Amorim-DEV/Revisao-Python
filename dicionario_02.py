""" Exercício 02
Preencha um dicionário com os dados de 5 alunos fornecidos pelo usuário.
- Solicite os dados do usuário
- Utilize o ra do aluno como chave e uma lista de três notas como valor.
- Percorra o dicionário e exiba a média de cada aluno.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]} """

notas = {}

continuacao = True

while continuacao:
    ra = int(input("Digite o RA do aluno: "))
    quantidade = int(input("Digite a quantidade de notas que serão inseridas: "))

    lista_notas = []  

    i = 0
    while i < quantidade:
        nota = float(input(f"Digite a {i+1}ª nota: "))
        lista_notas.append(nota)
        i += 1

    notas[ra] = lista_notas  

    continuar = input("Deseja adicionar mais alunos? y(yes) ou n(no): ").lower()

    if continuar not in ["y", "yes"]:
        continuacao = False

print("\nNotas e médias dos alunos:")
for ra, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)   
    print(f"RA {ra} → Notas: {lista_notas} | Média: {media:.2f}")

