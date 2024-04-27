# Libraries
import time
from clear import clear
from colorama import Fore

# Other quiz components
from intro import introduction
from functions_noncore_multidimensional import typing
from chess_easy import easy_quiz
from chess_hard import hard_quiz

# Main code.
typing(Fore.MAGENTA + "Welcome to the easy or hard chess quizzes. \n")
time.sleep(4)
clear()

# Make sure quiz_state is referenced from all introduction code.
quiz_state = introduction()

# User choose quiz.
while True:
    typing(Fore.GREEN + "Input 'easy' or 'hard' to start... \n")
    start = input().lower()

    if start in ["easy", "e"]:
        clear()
        typing(Fore.MAGENTA + "Commencing...")
        time.sleep(2)
        clear()
        # Pass the quiz_state object to the easy_quiz function
        easy_quiz(quiz_state)
        break

    if start in ["hard", "h"]:
        clear()
        typing(Fore.MAGENTA + "Commencing...")
        time.sleep(2)
        clear()
        hard_quiz(quiz_state)
        break

    else:
        print()
        typing(Fore.RED + "Please try again, only input 'easy' or 'hard'")
        time.sleep(0.8)
        clear()
        continue
