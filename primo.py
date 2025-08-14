def primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if numero % i ==0:
                return "Não é primo"
        return "É primo"

    else:
        return "Não é primo"
    
num = int(input("Digite um número para descobrir se ele é primo: "))
calculo = primo(num)
print(calculo)