class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def Still_Has_Questions(self):
        if self.question_number >= len(self.question_list):
            return False
        return True

    def Next_Question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(
            f"Q.{self.question_number}: {current_question.text} (True or False): ").lower()

        self.Check_Answer(ans, current_question.answer)

    def Check_Answer(self, guess, answer):
        if guess == answer.lower():
            print("Correct!")
            self.score += 1
            print(f"Score: {self.score}")
        else:
            print(f"Wrong! The correct answer is {answer}!")
            print(f"Final score: {self.score}")
