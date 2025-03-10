Velocidade = int(input("Velocidade"))
match Velocidade:
    case 80:
        print("Dentro do limite. Boa viagem!")
    case _ if Velocidade > 80:
         print(f'O pagamento é {(Velocidade - 80) * 2}')
