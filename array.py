from datetime import datetime
from random import randint, choice, shuffle, sample
from common import *
import time

number_of_questions = 5
timeout = 10
assessment = []

level = '3rd grade'
topic = 'Multiplication using arrays'
definition = 'The array below represents a product.'
ask = 'Which expression can be used to find the product represented by the array?'

start_time = datetime.now()
for i in range(1, number_of_questions + 1):
    x = randint(2, 12)
    y = randint(2, 12)

    correct_answer_1 = f'{x} x {y}'
    correct_answer_2 = f'{x} + ' * (y-1) + f'{x}'
    correct_answer = choice([correct_answer_1, correct_answer_2])
    incorrect_answer_1 = f'{x} + {y}'
    incorrect_answer_2 = f'{x} x ' * (y-1) + f'{x}'
    incorrect_answer_3 = f'{y} x ' * (x-1) + f'{y}'
    options = sample([incorrect_answer_1, incorrect_answer_2, incorrect_answer_3, correct_answer], 4)

    question = {
        'id':i,
        'question': options,
        'answer': correct_answer
    }

    while True:
        clear_screen()
        print_title(f'{level} - {topic}'.upper())
        print(f'You are answering the question {i} out of {number_of_questions}\n')
        print(definition)
        draw_array(x,y)
        print(f'\n{ask}\n')
        print_multi_choice(question['question'])
        user_answer = input("\n > ")
        try:
            user_answer = int(user_answer)
            if user_answer in range(1,5):
                question['user_answer'] = options[user_answer-1]
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
            else:
                raise ValueError
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
        Incorrect Answers:       {incorrect_answers}
        Score:                  {100*correct_answers/number_of_questions} %
        Time Spent:             {time_spent} minutes
''')