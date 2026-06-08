"""Text and image animations.
"""

import time
from IPython.display import clear_output

from modules import strings, animate, prof, route, pythodex

def write(text, speed=0.05):
    """Prints a string character-by-character.
    
    Parameters
    ----------
    text : str
        String to be printed.
        
    speed : int, default 0.05
        Speed of animation, in seconds. Dictates the pause after each character.
    
    Returns
    -------
    Prints the animated text.
    """

    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
        
def line(text, speed=0.2):
    """Prints a string line-by-line.
    
    Parameters
    ----------
    text : str
        String to be printed.
        
    speed : int, default 0.2
        Speed of animation, in seconds. Dictates the pause after each line.
    
    Returns
    -------
    Prints the animated text.
    """

    for line in text.splitlines():
        print(line)
        time.sleep(speed)

def reprint(image, text, speed=0.05, style="print"):
    """Prints an image, followed by text using the "write" animation. Typically used to 
    smoothly display new text under the same image.
    
    Parameters
    ----------
    image : str
        Image to be printed.

    text : str
        Text to be printed.
        
    speed : int, default 0.05
        Speed of text animation, in seconds. Dictates the pause after each character.
        
    style : string, default "print"
        The way to display the image. Value "print" displays the image with no animation.
        Value "line" prints the image line-by-line.
    
    Returns
    -------
    Prints the image and animated text.
    """

    if style == "print":
        clear_output(wait=True)
        print(image, flush=True)
        write(text, speed)

    elif style == "line":
        clear_output(wait=True)
        line(image)
        write(text, speed)