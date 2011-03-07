# PyRPG
# File: charcreation.py
# Version: 1.0
# Creator: Joel D. Garrett
# Modified: 3/4/2011

from gamestate import *
from player import *


def createNewPlayer():
    print "Welcome adventure. What is your name?"
    
    player = Player(raw_input())

    # Load player data
    if player.load() == False:
        print "Ahh! a new adventure! I will save your progress now."
        player.save()

    # Pause for reading
    print "\n-- Press any key to continue --"
    raw_input()

    return player
