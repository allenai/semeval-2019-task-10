import json
import os
import sys

class RandomGuesser:
    def __init__(self):
        pass

    def solve(self, question):
        if 'choices' in question:
            return 'A'
        else:
            return '0'

class ChoiceGuesser:
    def __init__(self, choice):
        self.choice = choice

    def solve(self, question):
        if 'choices' in question:
            return self.choice
        else:
            return None

class Conservative:
    def __init__(self):
        pass

    def solve(self, question):
        return None

def administer_questions(questions, student):
    answers = []
    for question in questions:
        guess = student.solve(question)
        if not guess is None:
            answer = {'id': question['id'], 'answer': guess}
            answers.append(answer)
    return answers

def write_answers_to_file(answers, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(answers, indent=4))


def main():

    # as per the metadata file, input and output directories are the arguments
    [_, input_file, output_file, student_name] = sys.argv

    if student_name == 'conservative':
        student = Conservative()
    elif student_name == 'a-guesser':
        student = ChoiceGuesser('A')
    elif student_name == 'b-guesser':
        student = ChoiceGuesser('B')
    elif student_name == 'c-guesser':
        student = ChoiceGuesser('C')
    elif student_name == 'd-guesser':
        student = ChoiceGuesser('D')
    elif student_name == 'e-guesser':
        student = ChoiceGuesser('E')
    else:
        raise ValueError('Student name not recognized: {}'.format(student_name))

    with open(input_file) as f:
        questions = json.load(f)
        answers = administer_questions(questions, student)
        write_answers_to_file(answers, output_file)


if __name__ == "__main__":
    main()


