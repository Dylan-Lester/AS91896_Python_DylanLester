# Libraries
import time
import random
from clear import clear

# Other quiz components
from questions import easy_questions
from functions_noncore_multidimensional import user_input
from functions_noncore_multidimensional import typing
from colorama import Fore
from end import end

# Gets every question from the dictionary.
easy_keys = list(easy_questions.keys())

# Randomises questions.
random.shuffle(easy_keys)


def easy_quiz(quiz_state):
    quiz_state.points = 0
    # Loop which goes through every question.
    for key in easy_keys:
        question = easy_questions[key]
        typing(Fore.BLUE + key)
        ans = input().lower()
        # If user answer equate to dictionary answer.
        if ans in question["Answer"]:
            quiz_state.points += 1
            print()
            typing(f"Right! Your total points are now {quiz_state.points}")
            time.sleep(1.5)
            clear()
        # Provides feedback
        else:
            print()
            typing(Fore.YELLOW +
                   f"Wrong!, {question['Explanation:']}")
            print()
            time.sleep(4)
            print()
            user_input()
            clear()

    time.sleep(1.5)
    typing(Fore.MAGENTA + "Your final point total is...")
    time.sleep(2)
    clear()

    typing(Fore.MAGENTA + f"{quiz_state.points}/10 \n")

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
