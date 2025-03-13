import requests
import json
import html
import random

class Question:
    def __init__(self, question, category, answers, correct_answer):
        self.question = question
        self.category = category
        self.answers = answers
        self.correct_answer = correct_answer




def get_questions(amount, diff_choice):
    if diff_choice == 1:
        difficulty = "easy"
    if diff_choice == 2:
        difficulty = "medium"
    if diff_choice == 3:
        difficulty = "hard"
    elif diff_choice > 3:
        difficulty = "hard"
    else:
        difficulty = "easy"

    response = requests.get(f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}")
    response.encoding = 'utf-8'
    data = json.loads(response.content.decode("utf-8"))
    questions = data["results"]
    q_objs = []
    for q in questions:
        answers = []
        answers.extend(html.unescape(q['incorrect_answers']))
        answers.append(html.unescape(q['correct_answer']))
        random.shuffle(answers)
        q_objs.append(Question(html.unescape(q['question']), html.unescape(q['category']), answers, html.unescape(q['correct_answer'])))
    return q_objs