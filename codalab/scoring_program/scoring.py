#!/usr/bin/env python
import sys
import os
import os.path
import json
import re

def isNumeric(string):
    try:
        f = float(string)
        return True
    except ValueError:
        return False
    

def readAnswersFromJson(filename, tag=None):
    with open(filename) as f:
        data = json.load(f)
    answers = dict()
    for i in range(len(data)):
        datum = data[i]
        if tag is None:
            answers[datum['id']] = datum['answer']
        elif tag in datum['tags']:
            answers[datum['id']] = datum['answer']
    return answers

def isCorrect(gold, candidate, margin_of_error = 0.01):
    letter_options = set(['A', 'B', 'C', 'D', 'E'])
    if gold.upper() in letter_options:
        return candidate.upper() == gold.upper()
    elif isNumeric(gold):
        if isNumeric(candidate):
            return abs(float(gold) - float(candidate)) < margin_of_error
        else:
            return False
    elif ' OR ' in gold:
        options = gold.split(' OR ')
        correctness = [isCorrect(opt, candidate, margin_of_error) for opt in options]
        return True in correctness
    elif re.search('\((.*),(.*)\)', gold) is not None:        
        m = re.search('\((.*),(.*)\)', gold)
        try:
            lbound = float(m.group(1))
            ubound = float(m.group(2))
            return float(candidate) > lbound and float(candidate) < ubound
        except ValueError:
            return False
    elif re.search('\\\\frac\s*\{([\s\d]+)\}\{([\s\d]+)\}', gold) is not None:
        m = re.search('\\\\frac\s*\{([\s\d]+)\}\{([\s\d]+)\}',  gold)
        numer = float(m.group(1))
        denom = float(m.group(2))
        return isCorrect(str(numer/denom), candidate, margin_of_error)    
    return False



def rawNumbers(gold_answers, answers):
    abstain = 0
    correct = 0
    incorrect = 0
    for question_id in gold_answers:
        if question_id in answers:
            if isCorrect(gold_answers[question_id], answers[question_id]):
                correct += 1
            else:
                incorrect += 1
        else:
            abstain += 1
    return correct, incorrect, abstain


def accuracy(correct, incorrect, abstain):
    total = correct + incorrect + abstain
    return correct/float(total)

def penalizedAccuracy(correct, incorrect, abstain, penalty = 0.2):
    total = correct + incorrect + abstain
    return (correct - incorrect * penalty) / float(total)

def scoreOld(gold_file, candidate_file, output_file, tag):
    gold_answers = readAnswersFromJson(gold_file, tag)
    answers = readAnswersFromJson(candidate_file)
    correct, incorrect, abstain = rawNumbers(gold_answers, answers)
    acc = accuracy(correct, incorrect, abstain)
    penal_acc = penalizedAccuracy(correct, incorrect, abstain)
    with open(output_file, 'w') as outhandle:
        outhandle.write('accuracy: {}\n'.format(acc))
        outhandle.write('penalized_accuracy: {}\n'.format(penal_acc))

def score(gold_file, candidate_file, output_file):
    answers = readAnswersFromJson(candidate_file)
    acc = dict()
    penal_acc = dict()
    for tag in ['closed', 'open', 'geometry']:
        gold_answers = readAnswersFromJson(gold_file, tag)
        correct, incorrect, abstain = rawNumbers(gold_answers, answers)
        acc[tag] = accuracy(correct, incorrect, abstain)
        penal_acc[tag] = penalizedAccuracy(correct, incorrect, abstain)
    gold_answers = readAnswersFromJson(gold_file, None)
    correct, incorrect, abstain = rawNumbers(gold_answers, answers)
    acc['all'] = accuracy(correct, incorrect, abstain)
    penal_acc['all'] = penalizedAccuracy(correct, incorrect, abstain)
    with open(output_file, 'w') as outhandle:
        outhandle.write('accuracy: {}\n'.format(acc['all']))
        outhandle.write('penalized_accuracy: {}\n'.format(penal_acc['all']))
        outhandle.write('closed_accuracy: {}\n'.format(acc['closed']))
        outhandle.write('closed_penalized_accuracy: {}\n'.format(penal_acc['closed']))
        outhandle.write('open_accuracy: {}\n'.format(acc['open']))
        outhandle.write('open_penalized_accuracy: {}\n'.format(penal_acc['open']))
        outhandle.write('geo_accuracy: {}\n'.format(acc['geometry']))
        outhandle.write('geo_penalized_accuracy: {}\n'.format(penal_acc['geometry']))

        
assert(isCorrect('A', 'A'))
assert(isCorrect('A', 'a'))
assert(isCorrect('E', 'E'))
assert(not(isCorrect('B', 'E')))

assert(isCorrect('0.55', '0.55'))
assert(not(isCorrect('0.55', '0.65')))
assert(not(isCorrect('0.55', '0.45')))

assert(isCorrect('2 OR 3', '3'))
assert(not(isCorrect('2 OR 3', '4')))
assert(isCorrect('2.4 OR 3.5 OR 5.4', '5.4'))
assert(isCorrect('2.4 OR 3.5 OR 5.4', '2.4'))
assert(not(isCorrect('2.4 OR 3.5 OR 5.4', '3.4')))

assert(isCorrect('(2, 4.2)', '3'))
assert(not(isCorrect(' (2, 4.2)', '4.3')))
assert(not(isCorrect('(a, 4.2', '3')))
assert(not(isCorrect('(a, 4.2)', '3')))

assert(isCorrect('\\(\\frac{3}{4}\\)', '0.75'))
assert(not(isCorrect('\\(\\frac{3}{4}\\)', '0.7')))
assert(isCorrect('\\(\\frac { 3 }{ 4 } \\)', '0.75'))

assert(isCorrect('(4, 6) OR 4 OR 6', '4.1'))
assert(not(isCorrect('(4, 6) OR 4 OR 6', '3.9')))
assert(isCorrect('(4, 6) OR 4 OR 6', '4'))
assert(not(isCorrect('(4, 6) OR 6', '4')))

assert(isCorrect('\\(\\frac{3}{4}\\) OR 0.73', '0.75'))
assert(isCorrect('\\(\\frac{3}{4}\\) OR 0.73', '0.73'))
assert(not(isCorrect('\\(\\frac{3}{4}\\) OR 0.73', '0.74')))


def main():
    
    # as per the metadata file, input and output directories are the arguments
    [_, input_dir, output_dir] = sys.argv
    
    # unzipped submission data is always in the 'res' subdirectory
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
    submission_file_name = 'answer.json'
    submission_dir = os.path.join(input_dir, 'res')
    submission_path = os.path.join(submission_dir, submission_file_name)
    print('executing scoring.py!')
    if not os.path.exists(submission_path):
        message = "Expected submission file '{0}', found files {1}"
        sys.exit(message.format(submission_file_name, os.listdir(submission_dir)))
    with open(submission_path) as submission_file:
        submission = submission_file.read()
    
    # unzipped reference data is always in the 'ref' subdirectory
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
    truth_path = os.path.join(input_dir, 'ref', 'truth.json')
    output_path = os.path.join(output_dir, 'scores.txt')
   
    score(truth_path, submission_path, output_path)

if __name__ == "__main__":
    main()
