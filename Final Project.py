from random import random
import random
from time import sleep
trivia_questions = {
    "Animal" : [
        {
            "question": "Que animal tem pupilas retangulares??",
            "options": ["Pinguins", "Cabras", "Papagaio", "Macaco"],
            "answer": 2
        },
        {
            "question": "Qual parte do corpo dos elefantes tem mais de 40.000 músculos??",
            "options": ["tronco", "orelhas", "pernas", "estômago"],
            "answer": 1
        },
        {
            "question": "Qual animal tem 3 corações?",
            "options": ["galinha", "baleia", "polvo", "vaca"],
            "answer": 3
        },
    ],
    "Paises e Capitais" : [
        {
            "question": "Qual país tem a montanha mais alta acima do nível do mar??",
            "options": ["Bélgica", "Índia", "Bolívia", "Nepal"],
            "answer": 4
        },
        {
            "question": "Qual pais tem 3 capitais?",
            "options": ["Bolivia", "Africa du Sul", "Australia", "USA"],
            "answer": 2
        },
        {
            "question": "Qual país tem a capital mais ao sul do planeta ",
            "options": ["Nova Zelandia", "Chile", "Antartica", "Australia"],
            "answer": 1
        },
    ],
    "Comida" : [
        {
            "question": "Qual destas plantas é uma fruta?",
            "options": ["Tomate", "Batata", "Cenoura", "Cebola"],
            "answer": 1
        },
        {
            "question": "Qual destes produtos nunca expira?",
            "options": ["Leite Condensado", "Arroz", "Mel", "Batata"],
            "answer": 3
        },
        {
            "question": "O que foi a primeira planta cultivada no espaço?",
            "options": ["Tomate", "Batata", "Cenoura", "Cebola"],
            "answer": 2
        },
    ]
}
def ask_question():
    category = random.choice(list(trivia_questions.keys()))
    question_answer = random.choice(trivia_questions[category])
    print(f'Categoria: {category}')
    sleep(1)
    print(f'Question: {question_answer["question"]}')
    options = question_answer["options"]
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    answer = int(input("Escolhe a resposta 1-4 : "))
    correct_answer = question_answer["answer"]
    if answer == correct_answer:
        print("Certo")
        trivia_questions[category].remove(question_answer)
    else:
        print("Errado")
        trivia_questions[category].remove(question_answer)


while True:
    ask_question()
    if all(len(questions) == 0 for questions in trivia_questions.values()):
        break
        

