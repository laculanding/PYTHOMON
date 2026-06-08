"""Functions to run Pythodex section of the game.
"""

import random
import time
import string
from IPython.display import clear_output

from modules import strings, animate, prof, route, pythodex

def view_dex(player_dex, all_mon, new):
    """Displays Pythodex interface.
    
    Parameters
    ----------
    player_dex : list
        List of Pythomon the player has caught.
        
    all_mon : list
        List of all available Pythomon.

    new : bool
        Condition to check if partner Pythomon dialogue has been triggered.
    
    Returns
    -------
    Displays Pythodex image, available entries, and input field. Will show "???"
    in front of entry number if Pythomon has not been caught yet.
    """
    
    clear_output(wait=True)
    print(strings.pythodex_sprite, flush=True)

    print("Enter a number to view the Pythodex entry:\n", flush=True)

    if new == True:
        print("【0】???", flush=True)
    else:
        print("【0】PYPY", flush=True)
    
    for entry in all_mon:
        if entry in player_dex:
            print(("【" + str(entry["num"]) + "】" + entry["name"]), flush=True)
            
        elif entry not in player_dex:
            print(("【" + str(entry["num"]) + "】???"), flush=True)

    print(("\nEnter:【E】to CHECK PYTHODEX |【X】to QUIT"), flush=True)

def view_entry(dex, user_input, new):
    """Displays chosen Pythomon entry.
    
    Parameters
    ----------
    dex : list
        List of Pythomon the player has caught.
        
    user_input : str
        Player input.

    new : bool
        Condition to check if partner Pythomon dialogue has been triggered.
    
    Returns
    -------
    Displays Pythomon sprite and information. Will instead show message
    if Pythomon has not been caught.
    """
    
    clear_output(wait=True)

    present = [entry["num"] for entry in dex]

    if new == False:
        present.append("0")
    
    if user_input in present:
        if user_input == "0":
            print(strings.pythodex_pypy, flush=True)
            animate.line(strings.pypy_info)
            
        elif user_input == "1":
            print(strings.pythodex_squirrelif, flush=True)
            animate.line(strings.squirrelif_info)
            
        elif user_input == "2":
            print(strings.pythodex_booldog, flush=True)
            animate.line(strings.booldog_info)
            
        elif user_input == "3":
            print(strings.pythodex_meowtable, flush=True)
            animate.line(strings.meowtable_info)
            
        elif user_input == "4":
            print(strings.pythodex_tuptle, flush=True)
            animate.line(strings.tuptle_info)
            
        elif user_input == "5":
            print(strings.pythodex_piploop, flush=True)
            animate.line(strings.piploop_info)
            
    else:
        animate.reprint(strings.pythodex_sprite, "You have not found this Pythomon yet!\n")

    print("\nEnter【X】to RETURN.")

def check_dex(dex):
    """Checks player's Pythodex progress.
    
    Parameters
    ----------
    dex : list
        List of Pythomon the player has caught.
        
    Returns
    -------
    Prints professor dialogue depending on number of Pythomon caught. If all 
    5 Pythomon have been caught, completion sequence is displayed.
    """
    
    animate.reprint(strings.prof_sprite, ("Hey there! Let's see how your Pythodex has been coming along..."))
    time.sleep(2)

    count = (len(dex))

    if count == 0:
        animate.reprint(strings.prof_sprite, ("You haven't found any Pythomon yet! Make sure to walk through the tall grass!"))
        time.sleep(1)

    elif count in range(1, 5):
        animate.reprint(strings.prof_sprite, ("You've found " + str(count) + " Pythomon! Keep up the good work!"))
        time.sleep(1)

    elif count == 5:

        complete_animation()
        prof.dialogue(strings.pythodex_text)
        
        animate.reprint(strings.completion_sprite, strings.completion_text, style="line")
        time.sleep(1)
        print("\n\nPress ENTER to continue.")
        input()
        
def complete_animation():
    """Animation for completed Pythodex
    
    Returns
    -------
    Prints short star animation for when Pythodex has been completed.
    """
    
    animate.reprint(strings.prof_sprite, ("   ★ ☆ ★ ☆ ★ !"), speed=0.3)

    for x in range(1, 5):
        if x % 2 == 0:
            clear_output(wait=True)
            print(strings.prof_sprite, flush=True)
            print("   ★ ☆ ★ ☆ ★ !", flush=True)
            time.sleep(1)
        else:
            clear_output(wait=True)
            print(strings.prof_sprite, flush=True)
            print("   ☆ ★ ☆ ★ ☆ !", flush=True)
            time.sleep(1)    