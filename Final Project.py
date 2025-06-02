from time import sleep
Points = 0
print("Olá a todos por estarem aqui para outro jogo do QUIZ!")
Theme = int(input("Qual tema vais querer? Coloque 1 para Animais, 2 para Capitais, 3 para Paises, 4 para Comida, 5 para Filmes e 6 para Esportes."))
match Theme:
    case 1:
        print("Estás pronto para a Trivia sobre Animais?")
        sleep(2)
        print("Pergunta 1")
        print("qual é o animal que tem pupilas retangulares")
        sleep(2)
        pergunta1 = int(input("Coloque 1 para Macacos, 2 para Papagaios , 3 para Cabras e 4 para Pinguims"))
        match pergunta1:
            case 1:
                print("errado. -5 pontos")
                Points = Points - 5
                print(f"Pontos = {Points}")
                sleep(1)
            case 2:
                print("errado. -5 pontos")
                Points = Points - 5
                print(f"Pontos = {Points}")
                sleep(1)
            case 3:
                print("certo. +10 pontos")
                Points = Points + 10
                print(f"Pontos = {Points}")
                sleep(1)
            case 4:
                print("errado. -5 pontos")
                Points = Points - 5
                print(f"Pontos = {Points}")
                sleep(1)
        print("Pergunta 2. Qual parte do corpo do Elefante têm mais de 40,000 músculos?")
        sleep(2)
        pergunta2 = int(input("Coloque 1 para as Orelhas, 2 para o Tronque, 3 para as Pernas e 4 para o Estômago"))
        match pergunta2:
            case 1:
                print("errado. -5 pontos")
                Points = Points - 5
                print(f"Pontos = {Points}")
            case 2:
                print("certo. +10 pontos")
                Points = Points + 10
                print(f"Pontos = {Points}")
            case 3:
                print("errado. -5 pontos")
                Points = Points - 5
                print(f"Pontos = {Points}")
            case 4:
                print("errado. -5 pontos")
                Points = Points - 5
                print(f"Pontos = {Points}")
