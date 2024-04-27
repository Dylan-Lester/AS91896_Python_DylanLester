# Libraries
import time
import sys
import os
import subprocess
from clear import clear

# Other quiz components
from colorama import Fore
from functions_noncore_multidimensional import typing


def end(quiz_state):
    point_name = [[quiz_state.name, quiz_state.points]]
    final_name = point_name[0][0]
    final_point = point_name[0][1]
    while True:
        typing(Fore.GREEN + "Would you like to return to the beginning [yes/no] "
                            "or see the scoreboard? [s/scoreboard] \n")
        quiz_loop = input().lower()

        if quiz_loop in ["yes", "y"]:
            time.sleep(0.5)
            typing("The quiz is starting again...")
            time.sleep(2)
            clear()
            # Program goes to beginning.
            subprocess.call(sys.executable + ' "' + os.path.realpath("main.py") + '"')

        elif quiz_loop in ["no", "n"]:
            time.sleep(0.5)
            typing("Hope you enjoyed!")
            time.sleep(2)
            clear()
            sys.exit()

        elif quiz_loop in ["s", "scoreboard"]:
            time.sleep(0.5)
            typing(f"{final_name} has {final_point} points. \n")

        else:
            print()
            typing(Fore.RED + "Invalid input, please either put 'yes' or 'no'. \n")
            time.sleep(1.5)
            clear()
            continue
