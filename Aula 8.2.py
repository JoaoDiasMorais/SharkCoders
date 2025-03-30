numero1 = int(input("Escolhe um numero "))
numero2 = int(input("Escolhe outro numero "))
par_ou_impar = str(input("par ou impar?"))
if par_ou_impar == "par":
    if numero1 % 2 == 0:
        if (numero2 + 1) % 2 == 0:
            for x in range(numero1,numero2 + 1, 2):
                print(x)
        else:
            for x in range(numero1, numero2 + 1, 2):
                print(x)
else:
     if (numero2 + 1) % 2 == 0:
         for x in range(numero1, numero2 + 1, 2):
            print(x)
     else:
        for x in range(numero1, numero2 + 1, 2):
            print(x)
