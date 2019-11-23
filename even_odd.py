from datetime import datetime
from random import randint, choice, shuffle, sample
from common import *
import time

level = '3rd grade'
topic = ' Even and Odd'

number_of_questions = 20
timeout = 10
assessment = []

character = choice(['Lucy', 'Hela', 'Anna'])

def ask(counting_by, start, stop):
    print(f'''{character} is counting by {counting_by}s. She starts with the number {start} and stops at the number {stop}.
    Which number would {character} NOT count?\n''')


start_time = datetime.now()
for i in range(1, number_of_questions + 1):
    counting_by = randint(2, 12)
    start = randint(0,12)
    stop = start + counting_by * randint(5,12)
    numbers = [num for num in range(start, stop+1, counting_by)]
    question_text = f'''{character} is counting by {counting_by}s. She starts with the number {start} and stops at the number {stop}.
    Which number would {character} NOT count?\n'''

    correct_answer = choice(numbers) - 1
    incorrect_answer_1 = choice(numbers)
    incorrect_answer_2 = choice(numbers)
    incorrect_answer_3 = choice(numbers)
    options = sample([incorrect_answer_1, incorrect_answer_2, incorrect_answer_3, correct_answer], 4)

    question = {
    'id':i,
    'question': question_text,
    'answer': correct_answer,
    'options': options
    }

    while True:
        clear_screen()
        print_title(f'{level} - {topic}'.upper())
        print(f'You are answering the question {i} out of {number_of_questions}\n')
        ask(counting_by, start, stop)
        print_multi_choice(question['options'])
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
        Incorrect Answers:      {incorrect_answers}
        Score:                  {100*correct_answers/number_of_questions} %
        Time Spent:             {time_spent} minutes
''')

for question in assessment:
    print(f"""Question {question['id']+1}
    Q:              {question['question']}
    Correct Answer: {question['answer']}
    User Answer:    {question['user_answer']}
    Result:         {question['score']}
    """)