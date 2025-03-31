def sum(numeros):
    total = 0
    for x in numeros:
        total += x
        return(total)

def sub(numeros):
    total = 0
    for x in numeros:
        total -= x
        return(total)

def mult(numeros):
    total = 1
    for x in numeros:
        total *= x
        return(total)

def div(numeros):
    total = 1
    for x in numeros:
        total /= x
        return(total)
        print(total)

div()