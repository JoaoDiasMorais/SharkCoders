def sum(numeros):
    total = 0
    for x in numeros:
        total += x
    return(total)

def sub(numeros):
    total = numeros[0]
    for x in numeros[1:]:
        total -= x
    return(total)

def mult(numeros):
    total = 1
    for x in numeros:
        total *= x
    return(total)

def div(numeros):
    total = numeros[0]
    for x in numeros[1:]:
        total /= x
    return(total)

primeiro = int(input("Escolhe um numero para ser mudado na operacao: "))
segundo = int(input("Escolhe um numero para mudar o primeiro numero na operacao: "))
operacao = str(input("Escolhe a operacao: "))

if operacao == "mult":
    print(mult([primeiro,segundo]))
elif operacao == "sub":
    print(sub([primeiro,segundo]))
elif operacao == "div":
    print(div([primeiro,segundo]))
else:
    print(sum([primeiro,segundo]))

