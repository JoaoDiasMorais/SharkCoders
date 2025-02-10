ordenado=int(input("O que é o seu ordenado atual?"))
if ordenado <500:
    reajuste= ordenado*1.15
    print(reajuste)
elif ordenado <=1000:
    reajuste2= ordenado*1.1
    print(reajuste2)
else:
    reajuste3= ordenado*1.05
    print(reajuste3)
