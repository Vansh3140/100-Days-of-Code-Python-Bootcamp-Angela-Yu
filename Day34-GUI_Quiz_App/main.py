from question_model import Question
from data import question_data
from ui import QuizUI
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_ui = QuizUI(question_bank)

