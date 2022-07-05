"""This is the main function."""

from main_logic import userChoiceOptions
from second_logic import userWindow


def main_func():
    """This is the main function responsible for starting the program.
    """
    print("=====================\n\"Welcome to shop!\"")
    userWindow()
    userChoiceOptions()


main_func()
