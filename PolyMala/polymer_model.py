from data import polymers_data, polymer_quiz1_data

class Polymers:
    def __init__(self,name,abbreviation,monomer,type,property,use):
        self.name = name
        self.abbreviation = abbreviation
        self.monomer = monomer
        self.type = type
        self.property = property
        self.use = use

polymers_bank = []

for polymer in polymers_data:
    new_polymer_name = polymer['name']
    new_polymer_abbreviation = polymer['abbreviation']
    new_polymer_monomer = polymer['monomer']
    new_polymer_type = polymer['type']
    new_polymer_property = polymer['property']
    new_polymer_use = polymer['use']
    new_polymer = Polymers(new_polymer_name,new_polymer_abbreviation,new_polymer_monomer,new_polymer_type,new_polymer_property,new_polymer_use)
    polymers_bank.append(new_polymer)

class PolymersQuiz1:
    def __init__(self,question,answer,explanation):
        self.question = question
        self.answer = answer
        self.explanation = explanation

quiz1_bank = []

for quiz in polymer_quiz1_data:
    new_quiz_question = quiz['question']
    new_quiz_answer = quiz['answer']
    new_quiz_explanation = quiz['explanation']
    new_quiz = PolymersQuiz1(new_quiz_question,new_quiz_answer,new_quiz_explanation)
    quiz1_bank.append(new_quiz)