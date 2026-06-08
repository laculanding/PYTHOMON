"""Runs game instance.
"""

import random
import time
import string
from IPython.display import clear_output

from modules import strings, animate, prof, route, pythodex
    
animate.write("\t\t     Welcome to...")
animate.line(strings.title_font, 0.4)
animate.write("\t\t Press ENTER to begin.") 
input()

prof.dialogue(strings.intro_text_1)
animate.reprint(strings.pythodex_sprite, ("\nYou have obtained a PYTHODEX!"), style="line")
time.sleep(1)
print("\n\nPress ENTER to continue.")
input()  
prof.dialogue(strings.intro_text_2)

player_dex = []
nickname = ""

menu = True
section_r = False
section_p = False
quit = False

new = True

while True:
    while menu:
        clear_output(wait=True)
        print(strings.menu_font, flush=True)
        print(strings.menu_text, flush=True)
            
        action = input()
            
        if action.strip() == "1":
            section_r = True
            menu = False
                
        elif action.strip() == "2":
            section_p = True
            menu = False
                
        elif action.strip() == "3":
            quit = True
            menu = False
                
        else:
            animate.write("Please enter a valid input.")
            time.sleep(1)
            continue

    while section_r:
        while new:
            prof.dialogue(strings.route_text_1)
            nickname = prof.name_partner()
            prof.dialogue(strings.route_text_2)
                
            new = False
                
        inst = route.TallGrass()
        check = inst.move(player_dex, section_r, menu, nickname)
        section_r = check[0]
        menu = check[1]
            
            
    while section_p:
        pythodex.view_dex(player_dex, route.pythomon, new)
        action = input()

        if action.lower().strip() == "x":
            section_p = False
            menu = True
            continue
                
        elif action.lower().strip() == "e":
            pythodex.check_dex(player_dex)
            continue
                
        elif action in [str(x) for x in range(6)]:
            while bool(action) == True:
                pythodex.view_entry(player_dex, action, new)
                action_2 = input()

                if action_2.lower().strip() == "x":
                    break
                        
                else:
                    animate.write("Please enter a valid input.")
                    time.sleep(1)
                                
        else:
            animate.write("Please enter a valid input.")
            time.sleep(1)
            continue

    while quit:
        clear_output(wait=True)
        print(strings.quit_text)
        action = input()
            
        if action.lower().strip() == "q":
            clear_output(wait=True)
            animate.line(strings.goodbye)
            quit = False
                
        elif action.lower().strip() == "x":
            quit = False
            menu = True
                
        else:
            animate.write("Please enter a valid input.")
            time.sleep(1)
            continue           