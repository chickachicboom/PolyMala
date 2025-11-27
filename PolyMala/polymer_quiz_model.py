from polymer_model import polymers_bank,quiz1_bank
import random

class PolymerQuiz:
    def __init__(self,quiz_list,polymers_list):
        self.quiz_list = quiz_list
        self.polymers_list = polymers_list
        self.list = 0
        self.score = 0

    def still_has_quiz(self):
        return self.list < len(self.polymers_list)
    
    def polymer_quiz_1(self):
        random.shuffle(self.quiz_list)

        quiz = self.quiz_list[self.list]
        self.list += 1

        print(f"\n{self.list} - {quiz.question}")
        user_answer = input()
        self.check_answer(user_answer.capitalize(),quiz.answer)
        print(f"The answer is {quiz.answer}")
        print(f"({quiz.explanation})")

    def polymer_quiz_2(self):

        quiz2_bank = []

        for polymer in self.polymers_list:
            quiz2_bank.append(polymer)

        random.shuffle(quiz2_bank)

        self.current_polymer = quiz2_bank[self.list]
        quiz = self.current_polymer

        print(f"{self.list + 1} - {quiz.name}\n")

        for i in range(len(self.polymers_list)):
            polymer = self.polymers_list[i]
            print(f"({i + 1}) {polymer.abbreviation}")
        user_choice = int(input(f"\nFrom choices above, enter {quiz.name}'s abbreviation here: "))
        user_answer_polymer = self.polymers_list[user_choice - 1]
        user_answer = user_answer_polymer.abbreviation
        self.check_answer(user_answer,self.current_polymer.abbreviation)
        print(f"Correct answer is: {self.current_polymer.abbreviation}\n\n")

        print(f"(1) addition\n(2) condensation")
        user_choice = int(input(f"\nFrom choices above, enter {quiz.name}'s type here: "))
        if user_choice == 1:
            user_answer = "addition"
        else:
            user_answer = "condensation"
        self.check_answer(user_answer,self.current_polymer.type)
        print(f"Correct answer is: {self.current_polymer.type}\n\n")

        for i in range(len(self.polymers_list)):
            polymer = self.polymers_list[i]
            print(f"({i + 1}) {polymer.property}")
        user_choice = int(input(f"\nFrom choices above, enter {quiz.name}'s property here: "))
        user_answer_polymer = self.polymers_list[user_choice - 1]
        user_answer = user_answer_polymer.property
        self.check_answer(user_answer,self.current_polymer.property)
        print(f"Correct answer is: {self.current_polymer.property}\n\n")

        for i in range(len(self.polymers_list)):
            polymer = self.polymers_list[i]
            print(f"({i + 1}) {polymer.use}")
        user_choice = int(input(f"\nFrom choices above, enter {quiz.name}'s use here: "))
        user_answer_polymer = self.polymers_list[user_choice - 1]
        user_answer = user_answer_polymer.use
        self.check_answer(user_answer,self.current_polymer.use)
        print(f"Correct answer is: {self.current_polymer.use}\n\n")

        self.list += 1

    def check_answer(self,user_answer,correct_answer):

        if user_answer == correct_answer:
            print("True!")
            self.score += 1
        else:
            print("False!")