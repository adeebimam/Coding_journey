class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        # Return True if there are more questions
        return self.q_number < len(self.q_list)

    def next_question(self):
        # Ask the next question
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct):
        # Compare the user's answer with the correct answer
        if user_answer.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.q_number}")
