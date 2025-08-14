def calcaular_fatorial(numero):
    resultado = 1
    while numero >= 2:
        resultado *= numero
        numero -= 1
    
    return resultado

num = int(input("Digite um número para descobrir o fatorial dele: "))
calculo = calcaular_fatorial(num)
print(calculo)