"""Functions for introductory professor dialogue.
"""

import time
import string
from IPython.display import clear_output

from modules import strings, animate

def dialogue(text):
    """Prints professor dialogue with sprite, followed by input field to continue.
    
    Parameters
    ----------
    text : str
        String to be printed.
    
    Returns
    -------
    Prints the sprite, animated text, and input field.
    """
    
    for line in text:
        animate.reprint(strings.prof_sprite, line, speed=0.02)
        
        time.sleep(0.5) 
        
        print("\n\nPress ENTER to continue.")
        input()

def name_partner():
    """Prints professor dialogue for naming player's partner Pythomon.
    
    Returns
    -------
    Prints the sprite, animated text, and input field. Stores player's chosen nickname in "nickname" variable in game.py.
    """
    
    animate.reprint(strings.pypy_sprite, ("\nYou have obtained a PYPY!\n"), style="line")
    time.sleep(1)
    
    while True:
        animate.reprint(strings.pypy_sprite, ("What nickname would you like to give your PYPY?\n"))

        nickname = input()

        if not nickname.strip():
            animate.reprint(strings.pypy_sprite, "You can't give your partner a blank nickname!")
            time.sleep(1)
            continue

        animate.reprint(strings.pypy_sprite, (
            "Are you sure you would like to name PYPY \"" + nickname + "\"? \nYou will not able to change this later.【Y/N】")
                       )
        action = input()

        if action.lower() == "n":
            continue
        elif action.lower() == "y":
            return nickname
        else:
            animate.reprint(strings.pypy_sprite, "Please enter a valid input.")
            time.sleep(1)
            continue