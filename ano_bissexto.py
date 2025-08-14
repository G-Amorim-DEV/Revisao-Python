def calcular_ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        x = print(f"O {ano} é bissexto")
        return x 

    else:
        y= print(f"O {ano} não um ano é bissexto")
        return y
    

ano = int(input("Digite um ano para verificar se ele é bissexto ou não: "))
calculo = calcular_ano_bissexto(ano)
