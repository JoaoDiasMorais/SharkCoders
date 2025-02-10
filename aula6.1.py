instalacao = str(input("O que é o seu instalacao?"))
if instalacao == ("Residencial"):
    kWh = int(input("O que é a quantidade de kWh que consumiste?"))
    if kWh <500:
        pagamento = kWh*0.40
        print(pagamento)
    else:
        pagamento = kWh*0.65
        print("Paga" "pagamento")
if instalacao == ("Comercial"):
    kWh2 = int(input("O que é a quantidade de kWh que consumiste?"))
    if kWh2 < 1000:
        pagamento2 = kWh2*0.55
        print(pagamento2)
    else:
        pagamento2 = kWh2*0.60
        print(pagamento2)
if instalacao == ("Industrial"):
    kWh3 = int(input("O que é a quantidade de kWh que consumiste?"))
    if kWh3 < 5000:
        pagamento3 = kWh3*0.55
        print(pagamento3)
    else:
        pagamento3 = kWh3*0.60
        print(pagamento3)



