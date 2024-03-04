from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:  # каждый item это список text и answer
    question = Question(item['question'], item['correct_answer'])  # создаем объект класса Question
    question_bank.append(question)  # в новом списке класс будет его элементом
# получается question_bank это один объект для всех классов включенных в список
# Таким образом нам далее очень легко будет обращаться к значению каждого ответа и вопроса
# print(question_bank[0].question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\n"
      f"Your final score was: {quiz.score}/{quiz.question_number}")

#!!! одно из преимуществ ооп в том, что данный код мало что аффектит,
# мы просто подствили новый список данных (data) и получаем новый квиз.
# Я только поменял значения в квадратных скобках (при определении объекта question)
# на те, что соотв-ют новому списку и мой квиз погнал работать



