# PyRPG
# File: pyrpg.py
# Version: 1.0
# Creator: Joel D. Garrett
# Modified: 3/4/2011

import os
from gamestate import *
from mainmenu import *
from player import *
from charcreation import *

def main():
    currentState = kGameStateMainMenu

    # Enter character creation
    player = createNewPlayer()    

    while currentState > kGameStateExit:
        os.system('clear')

        print "%s you are standing at the gates of the town. What would you like to do?" % (player.name)

        # Display Main Menu
        player.printStats()

        if currentState == kGameStateMainMenu:
            currentState = MainMenu().display() 

        # TODO: Enter town

        # TODO: Enter world

        # Pause for reading
        if currentState != kGameStateExit:
            print "\n -- Press any key to continue --"
            raw_input()

    return 0

main()
