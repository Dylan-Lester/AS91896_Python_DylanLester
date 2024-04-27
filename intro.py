# Intro

# Libraries
import time
from clear import clear

# Other quiz components
from functions_noncore_multidimensional import user_input
from functions_noncore_multidimensional import typing
from colorama import Fore
from functions_noncore_multidimensional import QuizState


def introduction():
    # Initialize the QuizState object
    quiz_state = QuizState()
    run = True

    typing(Fore.BLUE + "What is your name? \n")
    name = input().lower()

    # Validate name.
    if not name.isalpha():
        typing(Fore.RED + "Your name is invalid, please input letters only. \n")
        time.sleep(0.5)
        clear()
        # Goes back to introduction.
        return introduction()

    # Make name capitalized.
    quiz_state.name = name.capitalize()
    typing(Fore.BLUE + f"Get ready to start the quiz {quiz_state.name}!")
    time.sleep(2)
    clear()

    # Get user age and what quiz difficulty they want.
    while run:
        try:
            typing((Fore.GREEN + "What is your age? \n"))
            age = int(input())

        # Handle non-integer inputs
        except ValueError:
            print()
            typing(Fore.RED + "Please only input numbers. \n")
            time.sleep(0.5)
            clear()
            continue

        # Determine quiz difficulty based on age
        if 6 < age <= 12:
            time.sleep(0.5)
            print()
            typing(Fore.BLUE + "The easy quiz is recommended for you, even if you are good at chess.")
            time.sleep(3)
            clear()

        elif 6 >= age:
            time.sleep(0.5)
            print()
            typing(Fore.RED + "That's not true.")
            time.sleep(3)
            clear()
            continue

        elif 12 < age <= 100:
            time.sleep(0.5)
            print()
            typing("If you're good at chess, then the hard quiz is recommended for you!")
            time.sleep(3)
            clear()

        elif 100 < age <= 110:
            time.sleep(0.5)
            print()
            typing("If you say so...")
            time.sleep(3)
            clear()

        elif age > 110:
            time.sleep(0.5)
            print()
            typing(Fore.RED + "That's not true.")
            time.sleep(3)
            clear()
            continue

        else:
            time.sleep(0.5)
            print()
            typing(Fore.MAGENTA + "This may not be the quiz for you... but it's suggested to choose the easy mode.")
            time.sleep(3)
            clear()

        typing(Fore.MAGENTA + "There are 10 questions in both quizzes and getting a question correct nets you a point.")
        print()
        time.sleep(4)
        user_input()
        run = False

    # Return quiz_state at the end of the function.
    return quiz_state
