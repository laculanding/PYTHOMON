"""Functions to run route section of the game.
"""

import random
import time
import string
from IPython.display import clear_output

from modules import strings, animate, prof, route, pythodex

pythomon = [
    {"name" : "SQUIRRELIF", "hp" : 10, "sprite" : strings.squirrelif_sprite , "num" : "1"},
    {"name" : "BOOLDOG", "hp" : 14, "sprite" : strings.booldog_sprite, "num" : "2"},
    {"name" : "MEOWTABLE", "hp" : 13, "sprite" : strings.meowtable_sprite, "num" : "3"},
    {"name" : "TUPTLE", "hp" : 15, "sprite" : strings.tuptle_sprite, "num" : "4"},
    {"name" : "PIPLOOP", "hp" : 12, "sprite" : strings.piploop_sprite, "num" : "5"}
    
]

class TallGrass():
    """Handles tall grass mechanics, including display, player movement, and random encounter chance.
    
    Attributes
    ----------
    grid_size : int
        Length and width of tall grass patch.

    player_x : int
        Player's x-coordinate relative to the grid.

    player_y : int
        Player's y-coordinate relative to the grid.
    """
    
    def __init__(self):
        self.grid_size = 5
        self.player_x = 0
        self.player_y = 0
    
    def print_grid(self, grid_size, player_x, player_y):
        print("Enter:【WASD】to MOVE |【X】to QUIT\n", flush=True)
        
        for y in range(self.grid_size):
            row = ""
            
            for x in range(self.grid_size):
                if x == self.player_x and y == self.player_y:
                    row += " 𖨆  "
                    
                else:
                    row += r"\|/ "
                    
            row += "\n"
            print(row, flush=True)

    def random_encounter(self, dex, partner):
        x = (random.choices([True, False], weights =[0.25, 0.75], k = 1))
        check = x[0]

        if check == True:
            time.sleep(0.5)
            encounter(dex, partner)
    
    def move(self, dex, off, on, partner):
        while True:
            clear_output(wait=True)
            self.print_grid(self.grid_size, self.player_x, self.player_y)
            time.sleep(0.05)
            action = input()
        
            if action.lower() == 'x':
                return [False, True]
                
            elif action.lower() == 'a' and self.player_x > 0:
                self.player_x -= 1
                self.random_encounter(dex, partner)
                
            elif action.lower() == 'd' and self.player_x < self.grid_size - 1:
                self.player_x += 1
                self.random_encounter(dex, partner)
                
            elif action.lower() == 'w' and self.player_y > 0:
                self.player_y -= 1
                self.random_encounter(dex, partner)
                
            elif action.lower() == 's' and self.player_y < self.grid_size - 1:
                self.player_y += 1
                self.random_encounter(dex, partner)
                
            else:
                clear_output(wait=True)
                self.print_grid(self.grid_size, self.player_x, self.player_y)
                animate.write("\nYou can't go there!")
                time.sleep(0.5)

class Opponent():  
    """Information about opponent Pythomon in battle.
    
    Attributes
    ----------
    name : str
        Name of opponent Pythomon.

    hp : int
        Total health points of opponent Pythomon.

    sprite : str
        Image of opponent Pythomon.

    current_hp : int
        Current health points of opponent Pythomon. Updated via take_dmg() class method.

    catch_rate : float
        Probability of opponent Pythomon being caught. Updated via throw_ball() class method
        based on current HP.
    """
    
    def __init__(self, name, health, sprite):
        self.name = name
        self.hp = health
        self.sprite = sprite
        self.current_hp = self.hp
        self.catch_rate = 0.25

    def reprint_opp(self, new=False, text=None, sec=1):
        clear_output(wait=True)
            
        if new == True:
            animate.line(self.sprite + "\n" + self.name + ("\n〈 HP: " + str(self.current_hp) + " / " + str(self.hp) + " 〉\n"))
        else:
            print(self.sprite + "\n" + self.name + ("\n〈 HP: " + str(self.current_hp) + " / " + str(self.hp) + " 〉\n"), flush=True)
            animate.write(text, 0.025)
            time.sleep(sec)
            
    def take_dmg(self):
        dmg = random.choice(range(2,5))
        self.current_hp = self.current_hp - dmg
        
        if self.current_hp < 0:
            self.current_hp = 0

    def throw_ball(self):

        proportion = self.current_hp / self.hp

        if proportion <= 0.30:
            self.catch_rate = 0.95
        elif proportion <= 0.50:
            self.catch_rate = 0.75
        elif proportion <= 1.00:
            self.catch_rate = 0.40

        bools = [True, False]
        catch = random.choices(bools, weights=[(self.catch_rate), (1 - self.catch_rate)], k=1)

        return catch[0]

    def add_to_dex(self, dex):
        for x in pythomon:
            if self.name == x["name"]:
                dex.append(x)
                           
def find():
    """Decides on the opponent wild Pythomon based on weighted probabilities.
    
    Returns
    -------
    wild : Opponent
        The chosen Pythomon as an initialized instance.
    """
    
    x = (random.choices(pythomon, weights=[0.30, 0.30, 0.15, 0.15, 0.10], k=1))
    info = x[0]
    wild = Opponent(info["name"], info["hp"], info["sprite"])
    return wild

def attack(opp, partner):
    """Uses attack on opponent Pythomon.
    
    Parameters
    ----------
    opp : Opponent
        Opponent wild Pythomon.
        
    partner : str
        Partner Pythomon's nickname.
    
    Returns
    -------
    Prints attack message. Lowers opponent Pythomon's health. Opponent Pythomon faints
    if health reaches 0.

    bool
        Condition to end the encounter.
    """
    
    opp.reprint_opp(text=(partner + " used CYBER ATTACK!"))
    opp.take_dmg()

    if opp.current_hp == 0:
        opp.reprint_opp(text=("The wild " + opp.name + " fainted!"), sec=2)
        return False

    return True

def catch(opp, dex):
    """Attempts to catch opponent Pythomon.
    
    Parameters
    ----------
    opp : Opponent
        Opponent wild Pythomon.
        
    dex : list
        List of Pythomon the player has caught already.
    
    Returns
    -------
    Uses Opponent.throw_ball() to decide if catch is successful. If success, ends encounter and
    adds opponent Pythomon's information to Pythodex if not already present. If fail, continues
    encounter.

    bool
        Condition to end the encounter.
    """
    
    opp.reprint_opp(text=("You threw a Pythoball!"))
    result = opp.throw_ball()

    for x in range(1,4):
        opp.reprint_opp(text=(". " * x))
        
    if result == False:
        opp.reprint_opp(text=("Oh no! The wild " + opp.name + " broke free!"))
        return True
                
    elif result == True:
        opp.reprint_opp(text=("Gotcha! You caught a " + opp.name + "!"))

        present = []

        for x in dex:
            present.append(x["name"])

        if opp.name not in present:
            opp.reprint_opp(text=(opp.name + " has been added to your Pythodex."))
            opp.add_to_dex(dex)
                
        return False

def encounter(dex, partner):
    """Displays wild encounter interface.
    
    Parameters
    ----------
    dex : list
        List of Pythomon the player has caught.
        
    partner : str
        Partner Pythomon's nickname.
    
    Returns
    -------
    Uses Opponent.throw_ball() to decide if catch is successful. If success, ends encounter and
    adds opponent Pythomon's information to Pythodex if not already present. If fail, continues
    encounter.
    """

    battle = True
    
    wild = find()
    
    clear_output(wait=True)
    animate.line(strings.encounter_notif)
    time.sleep(1)
    
    wild.reprint_opp(new=True)
    animate.line("\n")
    animate.write("A wild " + wild.name + " appeared!")
    time.sleep(1)

    
    while battle:
        wild.reprint_opp(text=("What will " + partner +" do?"))
        print(strings.battle_text, flush=True)
    
        action = input()
        
        if action.strip() == "1":
            battle = attack(wild, partner)
                                    
        elif action.strip() == "2":
            battle = catch(wild, dex)
              
        elif action.strip() == "3":
            wild.reprint_opp(text=("You got away safely!"))
            time.sleep(1)
            battle = False
            
        else:
            wild.reprint_opp(text=("Please enter a valid input."))
            time.sleep(1)
            print(strings.battle_text, flush=True)
            continue