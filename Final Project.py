from random import random
import random
from time import sleep
trivia_questions = {
    "Animal" : [
        {
            "question": "What Animal Has Rectangular Pupils?",
            "options": ["Penguins", "Goats", "Parrots", "Monkeys"],
            "answer": 2
        },
        {
            "question": "Which part of the elephants body has over 40,000 muscles?",
            "options": ["Trunk", "Ears", "Legs", "Stomach"],
            "answer": 1
        },
        {
            "question": "Which Animal Has 3 Hearts",
            "options": ["Chicken", "Whale", "Octopus", "Cow"],
            "answer": 3
        },
    ],
    "Capitals" : [
        {
            "question": "What Country has the highest mountain above sea level?",
            "options": ["Belgium", "India", "Bolivia", "Nepal"],
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

