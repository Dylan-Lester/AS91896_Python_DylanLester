# Libraries
import time
import sys
from clear import clear
import msvcrt

# Other quiz components
from colorama import Fore

# Letter by letter effect for all typing not done by user.


def typing(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


# Function for user where they must press enter to continue the program at certain points.

def user_input():
    typing(Fore.WHITE + "Press enter to continue... \n")
    # Use msvcrt import to only allow user to enter if the key pressed is enter.
    while True:
        key = msvcrt.getch()
        if key == b'\r':  # Byte representation of the enter key.
            break
    clear()


# Lets points from the quiz and name from the intro be usable in end.py
# initializes the name and points class (starting them at 0 and no name).

class QuizState:
    def __init__(self):
        self.name = None
        self.points = 0
