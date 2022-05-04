
from unittest import result
from urllib import response
import requests
import time
from unicodedata import category
import json
import random


HISTORY_URL = "https://opentdb.com/api.php?amount=5&category=23&difficulty=easy&type=multiple"

SPORTS_URL = "https://opentdb.com/api.php?amount=5&category=21&difficulty=easy&type=multiple"

CARS_URL = "https://opentdb.com/api.php?amount=5&category=28&difficulty=easy&type=multiple"


# response = requests.get(HISTORY_URL).json()

# print(json.dumps(response['results'],indent = 2))

categories = {
    '1': 'History',
    '2': 'Sports',
    '3': 'Cars'
}

print("Hi there!\n")
time.sleep(1)
print("Let's play Trivia...\n")
time.sleep(1)

while True:
    print("\nHere are your categories: ")
    # time.sleep(1)
    for key in categories.keys():
        time.sleep(1)
        print(f"{key}. {categories[key]}")
    # time.sleep(1)    
    user_choice = input("\nPick a category:\n ")

    while user_choice  not in categories.keys():
        time.sleep(1)
        print("That category does not exsist...")
        time.sleep(1)
        print("\nPlease choose from one of the following options: ")
        time.sleep(1)
        for key in categories.keys():
            time.sleep(1)
            print(f"{key}. {categories[key]}")
        # time.sleep(1)
        user_choice = input("\nPick a category:\n ")

    if user_choice == '1':
        data_pull = requests.get(HISTORY_URL)
        
    elif user_choice == '2':
        data_pull = requests.get(SPORTS_URL)

    elif user_choice == '3':
        data_pull = requests.get(CARS_URL)


    data = data_pull.json()


    question_data = data['results']

    score = 0

    question_number = 0

    for question in question_data:

        question_data = question['question']
        correct_answer = question['correct_answer']
        incorrect_answers = question['incorrect_answers']

        question_number += 1

        time.sleep(1)
        print(f"\nQuestion {question_number}: {question_data}")  #add a loop that will state the question

        answer_choices = []
        answer_choices.append(correct_answer)
        for answer in incorrect_answers:
            answer_choices.append(answer)

        random.shuffle(answer_choices)

        for index in range(len(answer_choices)):
            time.sleep(1)
            print(f"\n{index+1}. {answer_choices[index]}")

        # time.sleep(2)
        user_input = input("\nType your answer number here: \n")

        user_input = int(user_input)

        while user_input < 1 or user_input > 4: #ncreate a failsafe for user input to not be number choice
            # time.sleep(1)
            print("\nThat is an incorrect response...\n\nPlease choose from the following:\n")

            for index in range(len(answer_choices)):
                time.sleep(1)
                print(f"\n{index+1}. {answer_choices[index]}")

            user_input = input("\nType your answer number here: \n")

            user_input = int(user_input)

        if user_input-1 == answer_choices.index(correct_answer):
            print('\nYou are correct!\n\n1 point has been added to your overall score')
            score += 1
            print(f"Running score: {score}")
        else:
            print('\nThat answer is incorrect...\n\n0 points have been added to your overall score')
            print(f"Running score: {score}")

    print(f"\nYour total score is {score}!\n")

    continue_response = input("Would you like to play again? Enter yes or no: ")

    if continue_response == 'yes':
        continue
    else:
        print('\nThanks for playing Trivia!')
    break




























'''create a loop that will run through each item in results list for key of question and answers:
1. show the qestion
2. show the answer options
3. take in user input
4. compare user input with correct_answer
5. print correct or incorrect'''
