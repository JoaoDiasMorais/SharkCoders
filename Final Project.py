from random import random
import random
from time import sleep
trivia_question = {
    "Animal" : [
    {
        "question": "What Animal Has Rectangular Pupils?",
        "options": ["Penguins", "Goats", "Parrots", "Monkeys"],
        "answer": "Goats"
    },
    {
        "question": "Which part of the elephants body has over 40,000 muscles?",
        "options": ["Trunk", "Ears", "Legs", "Stomach"],
        "answer": "Trunk"
    },
    {
        "question": "Which Animal Has 3 Hearts",
        "options": ["Chicken", "Whale", "Octopus", "Cow"],
        "answer": "Octopus"
    },
] }
def questions():
    category = random.choice(list(trivia_question.keys()))
    question = random.choice(trivia_question[category])

    print(f'Categoria: {category}')
    sleep(1)
    print(f'Question: {question}')
    options = question["options"]
    for i, option in enumerate(options):
        print(f"f.{i+1}, {option}")
    answer = int(input("Insert your number 1-4"))
    if answer == options["answer"]:
        print("Correct")
    else:
        print("Wrong")


questions()

