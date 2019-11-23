from datetime import datetime
from random import randint
from common import *
import time

number_of_questions = 100
timeout = 10
assessment = []

start_time = datetime.now()
for i in range(1, number_of_questions + 1):
    factor_1 = randint(0,12)
    factor_2 = randint(0,12)
    product = factor_1 * factor_2

    question = {
        'id':i,
        'question': f'{factor_1} x {factor_2} = ',
        'answer': factor_1 * factor_2
    }

    while True:
        try:
            clear_screen()
            print_title('multiplications test'.upper())
            print(f'You are answering the question {i} out of {number_of_questions}\n')
            user_answer = input(f"{question['question']}")
            user_answer = int(user_answer)
            question['user_answer'] = user_answer
            if question['answer'] == question['user_answer']:
                question['score'] = 'PASS'
                print('\nBingo!\n'.upper())
                time.sleep(1)
            else:
                question['score'] = 'FAIL'
                print('\nWhoopsie!\n'.upper())
                time.sleep(1)
            assessment.append(question)
            break
        except ValueError:
            print(f'[{user_answer}] is not a valid entry. Please try again ')
            continue
end_time = datetime.now()
time_spent = (end_time - start_time).total_seconds() / 60.0

correct_answers = len([question['score'] for question in assessment if question['score'] == 'PASS'])
incorrect_answers = len([question['score'] for question in assessment if question['score'] == 'FAIL'])
print(f'''
        Total Questions:        {number_of_questions}
        Correct Answers:        {correct_answers}
        Incorrect Answers:      {incorrect_answers}
        Score:                  {100*correct_answers/number_of_questions} %
        Time Spent:             {time_spent} minutes
''')

for question in assessment:
    print(f"{question['question']} = {question['answer']} | {question['user_answer']} | {question['score']}")