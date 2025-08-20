import os 

""" Exercício 02
Preencha um dicionário com os dados de 5 alunos fornecidos pelo usuário.
- Solicite os dados do usuário
- Utilize o ra do aluno como chave e uma lista de três notas como valor.
- Percorra o dicionário e exiba a média de cada aluno.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]} """

notas = {}

k = 0
while k < 5:
    while True:
        try:
            ra = int(input(f"Digite o RA do {k+1}º aluno: "))
            if ra > 0:
                break
            else:
                print("O RA deve ser um número inteiro maior que zero.")
        except ValueError:
            print("Digite um valor inteiro para o RA.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade de notas que serão inseridas: "))
            if quantidade > 0:
                break
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Digite um valor inteiro para a quantidade.")

    lista_notas = []
    i = 0
    while i < quantidade:
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))
            if nota > 0:
                lista_notas.append(nota)
                i += 1
            else:
                print("A nota deve ser maior que zero.")
        except ValueError:
            print("Digite uma nota válida (número inteiro ou decimal).")

    notas[ra] = lista_notas
    k += 1

print("\nNotas e médias dos alunos:")
for ra, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"RA {ra} → Notas: {lista_notas} | Média: {media:.2f}")