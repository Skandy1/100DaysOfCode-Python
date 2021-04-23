from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for x in question_data:
    new_obj=Question(x["question"],x["correct_answer"])
    question_bank.append(new_obj)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz! Thanks for participating!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
