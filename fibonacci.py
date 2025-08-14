def fibonacci(numero):
    sequencia = []
    a, b = 0, 1

    for _ in range(numero):
        sequencia.append(a)
        a, b = b, a + b

    return sequencia

num = int(input("Digite quantos números da sequência de Fibonacci você quer ver: "))
calculo = fibonacci(num)
print(f"Os {num} primeiros números da sequência de Fibonacci são:")
print(calculo)
