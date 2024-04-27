# Libraries.
import time
import random
from clear import clear

# Other quiz components
from questions import hard_questions
from functions_noncore_multidimensional import user_input
from functions_noncore_multidimensional import typing
from colorama import Fore
from end import end

# Gets every question from the dictionary.
hard_keys = list(hard_questions.keys())

# Randomises questions.
random.shuffle(hard_keys)


def hard_quiz(quiz_state):
    quiz_state.points = 0
    # Loop which goes through every question.
    for key in hard_keys:
        question = hard_questions[key]
        typing(Fore.RED + key)
        ans = input().lower()
        # If user answer equate to dictionary answer.
        if ans in question["Answer"]:
            quiz_state.points += 1
            print()
            typing(f"That's correct, your point total is {quiz_state.points}")
            time.sleep(1.5)
            clear()
        else:
            print()
            typing(Fore.YELLOW +
                   f"That is incorrect, {question['Explanation:']}")
            print()
            time.sleep(4)
            print()
            user_input()
            clear()

    time.sleep(2)
    typing("Your final score is...")
    time.sleep(2)
    clear()

    typing(f"{quiz_state.points}/10 \n")

    if 4 >= quiz_state.points:
        time.sleep(2)
        typing("Hopefully you've learned something. \n")

    elif 5 <= quiz_state.points <= 7:
        time.sleep(2)
        typing("You did pretty good. \n")

    elif 8 <= quiz_state.points <= 9:
        time.sleep(2)
        typing("You did amazing. \n")

    else:
        time.sleep(2)
        typing("You must really know your stuff to get 10/10 \n")

    time.sleep(3)
    clear()

    end(quiz_state)
