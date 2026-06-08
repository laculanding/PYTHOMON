"""Long text strings used in-game. Stored here to reduce clutter.
"""

title_font = r"""
 
█████▄ ██  ██ ██████ ██  ██ ▄████▄ ██▄  ▄██ ▄████▄ ███  ██ 
██▄▄█▀  ▀██▀    ██   ██████ ██  ██ ██ ▀▀ ██ ██  ██ ██ ▀▄██ 
██       ██     ██   ██  ██ ▀████▀ ██    ██ ▀████▀ ██   ██   
 
"""

prof_sprite = r"""
     ///////\
   / | ^   ^ | \
   |(| O---O |)| 
   ) |   ~   | (
  (   \  ᗜ  /   )
   )//__|_|__\\(
    /         \
"""

intro_text_1 = [
    "\"Hello! My name is Professor Jupyter. I research Pythomon——the \nmysterious creatures we share the world with.\"",
    "\"I called you here to my lab today because I would like to ask \nyou for your help with something.\"",
    "\"The route outside your town is home to 5 particular Pythomon \nspecies I am currently interested in. Your job is to catch each \nof these species and record them in this device.\""
]

intro_text_2 = [
    "\"This is a Pythodex! It automatically stores information about \nall the different Pythomon you encounter. Having this data would \nbe a great help for my research!\"",
    "\"Well, that's all for me. Come back to my lab if you would like \nme to check your Pythodex progress. Good luck!\""
]

route_text_1 = [
    "\"Hold on a second, I nearly forgot!\"",
    "\"Silly me, you don't have your own Pythomon yet, do you?\"",
    "\"Well, you can't catch wild Pythomon without a Pythomon partner \nof your own! So, here is a Pythomon called PYPY to help you!\""
]

route_text_2 = [
    "\"This PYPY here will battle other Pythomon for you. If you tell \nyour partner to attack, it will lower the opponent Pythomon's HP. \nThe lower the HP, the easier it is to catch! Cool, huh?\"",
    "\"Alright, I'll let you get to it now——for real this time. Have fun!\""
]

pypy_sprite = r"""
           __
(\   ,.   /_::)
 \\_//\\_//
  `"`   `"`
"""

menu_font = r"""   
▄▄   ▄▄ ▄▄▄▄▄ ▄▄  ▄▄ ▄▄ ▄▄ 
██▀▄▀██ ██▄▄  ███▄██ ██ ██ 
██   ██ ██▄▄▄ ██ ▀██ ▀███▀      
"""

menu_text = r"""         Enter:
【1】to go to the ROUTE.
【2】to view your PYTHODEX.
【3】to QUIT the game.
            """

encounter_notif = r"""            
 ▄▄  ▄▄  ▄▄ 
 ██  ██  ██ 
 ██  ██  ██ 
 ▄▄  ▄▄  ▄▄ 
 """

squirrelif_sprite = r"""
      __  (\_ 
     (_ \ ( '> 
       ) \/_)=
\|/__  (_(_ )_  __\|/
"""

booldog_sprite = r"""
            __
       (___V '`;
       /,    /`
\|/__  \\"--\\   __\|/
"""

meowtable_sprite = r"""
         ^~^  ,
        ('Y') )
        /   \/
\|/__  (\|||/)  __\|/
"""

tuptle_sprite = r"""
         _____  __
        /// //\/_'| 
       |_______/     
\|/__  |_|  |_|  __\|/
"""

piploop_sprite = r"""
        ___
       (  o>
       /// \
\|/__  \V__/_   __\|/ 
"""

battle_text = r"""
【1】ATTACK
【2】CATCH
【3】RUN
                    """

pythodex_sprite = r""" _______________________________   
/         ______________         \  
| == .   |              |      o |  
|   _    |              |   ( )  |  
|  /_\   |              |        |  
|  \_/   |              |   :::  |     
|        |______________|        | 
\________________________________/
"""

pythodex_pypy = r""" _______________________________   
/         ______________         \  
| == .   |           __ |      o |
|   _    |(\   ,.   /_")|   ( )  |
|  /_\   | \\_//\\_//   |        |
|  \_/   | `"`   `"`    |   :::  |
|        |______________|        | 
\________________________________/
"""

pypy_info = r"""         【No. 111】PYPY 
              
Coding Pythomon        HT  2'02"
RARITY ★★★★          WT  12.1 lbs

It has the ability convert its body into 
digital data, which enables it to enter 
and move freely through cyberspace."""

pythodex_squirrelif = r""" _______________________________   
/         ______________         \  
| == .   |       (\_    |      o |
|   _    |  (_ \ ( '>   |   ( )  |
|  /_\   |    ) \/_)=   |        | 
|  \_/   |    (_(_ )_   |   :::  |
|        |______________|        | 
\________________________________/
"""

squirrelif_info = r"""      【No. 001】SQUIRRELIF 
              
Peckish Pythomon       HT  1'00"
RARITY ★               WT  8.6 lbs

Its favorite food are Numpy Berries. But 
because these berries are rare, it is often 
found munching on Pandas Berries instead."""

pythodex_booldog = r""" _______________________________   
/         ______________         \  
| == .   |        __    |      o |
|   _    |   (___V '`;  |   ( )  |
|  /_\   |   /,    /`   |        |
|  \_/   |   \\"--\\    |   :::  |
|        |______________|        | 
\________________________________/
"""

booldog_info = r"""       【No. 002】BOOLDOG 
              
Polygraph Pythomon     HT  1'05"
RARITY ★               WT  14.4 lbs

It has a very sensitive nose that can detect 
chemical signals that indiciate whether or 
not someone is telling the truth."""

pythodex_meowtable = r""" _______________________________   
/         ______________         \  
| == .   |     ^~^  ,   |      o |
|   _    |    ('Y') )   |   ( )  |
|  /_\   |    /   \/    |        |
|  \_/   |   (\|||/)    |   :::  |
|        |______________|        | 
\________________________________/
"""

meowtable_info = r"""      【No. 003】MEOWTABLE 
              
Chameleon Pythomon     HT  1'08"
RARITY ★★             WT  9.6 lbs

It can change the color of its fur at will. 
It often uses this ability to blend in with 
its environment or communicate its mood."""

pythodex_tuptle = r""" _______________________________   
/         ______________         \  
| == .   |   _____  __  |      o |
|   _    |  /// //\/_'| |   ( )  | 
|  /_\   | |_______/    |        |  
|  \_/   | |_|  |_|     |   :::  |
|        |______________|        | 
\________________________________/
"""

tuptle_info = r"""        【No. 004】TUPTLE 
              
Loyal Pythomon         HT  1'04"
RARITY ★★             WT  22.5 lbs

Upon reaching maturity, they will form small, 
tight-knit social groups. These groups tend to 
last for life and will rarely take in new members."""

pythodex_piploop = r""" _______________________________   
/         ______________         \  
| == .   |     ___      |      o |
|   _    |    (  o>     |   ( )  |
|  /_\   |    /// \     |        |
|  \_/   |    \V__/_    |   :::  |
|        |______________|        | 
\________________________________/
"""

piploop_info = r"""        【No. 005】PIPLOOP 
              
Dancer Pythomon        HT  1'08"
RARITY ★★★            WT  11.5 lbs

Their mating rituals involve a set of 
flamboyant moves that is repeated until the 
potential mate gives a chirp as an answer."""

pythodex_text = [
    "\"Woah, you've done it! You found all 5 Pythomon! Awesome job!\"",
    "\"I'm very excited to use this in my research. After all, there's \nstill so much to learn about Pythomon! Thanks for all your help!\"",
    "\"Feel free to keep on battling and catching Pythomon in the \nmeantime. And by the way, I think you'll make a great Pythomon \ntrainer someday! Until next time!\""
]

completion_sprite = r"""
           __
(\   ,.   /_^^)
 \\_//\\_//
  `"`   `"`
"""
completion_text = [
    "Congrats! You have finished the game!",
    "You will now be returned to the menu. If you'd like, you can continue to \nvisit the route to encounter wild Pythomon. Otherwise, you may exit the game from the menu screen. Thanks for playing!"
]

quit_text = r"""
WARNING! Are you sure you want to quit? All progress will be lost.

         Enter:
【Q】to QUIT the game.
【X】to RETURN to the menu.
"""
goodbye = r"""                                                                                                 
                                                                                                      ▄▄ 
██████ ▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄  ▄▄▄▄   ▄▄▄▄▄  ▄▄▄  ▄▄▄▄    █████▄ ▄▄     ▄▄▄  ▄▄ ▄▄ ▄▄ ▄▄  ▄▄  ▄▄▄▄  ██ 
  ██   ██▄██ ██▀██ ███▄██ ██▄█▀ ███▄▄   ██▄▄  ██▀██ ██▄█▄   ██▄▄█▀ ██    ██▀██ ▀███▀ ██ ███▄██ ██ ▄▄  ██ 
  ██   ██ ██ ██▀██ ██ ▀██ ██ ██ ▄▄██▀   ██    ▀███▀ ██ ██   ██     ██▄▄▄ ██▀██   █   ██ ██ ▀██ ▀███▀  ▄▄ 
  
"""                                                                                                         