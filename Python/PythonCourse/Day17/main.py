from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_to_add = Question(q["question"], q["correct_answer"])
    question_bank.append(question_to_add)

my_question = QuizBrain(question_bank)

while my_question.Still_Has_Questions():
    my_question.Next_Question()

print("Quiz complete!")
print(
    f"Your final score is: {my_question.score}/{len(my_question.question_list)}\n")
