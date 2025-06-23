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
            "question": "Which country has 3 capitals?",
            "options": ["Bolivia", "South Africa", "Australia", "USA"],
            "answer": 2
        },
        {
            "question": "Which country has the capital most to the most south on the planet",
            "options": ["New Zealand", "Chile", "Antartica", "Australia"],
            "answer": 1
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
    answer = int(input("Insert your number 1-4 : "))
    correct_answer = question_answer["answer"]
    if answer == correct_answer:
        print("Correct")
    else:
        print("Wrong")

while True:
    ask_question()

