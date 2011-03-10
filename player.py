# PyRPG
# File: player.py
# Version: 1.0
# Creator: Joel D. Garrett
# Modified: 3/5/2011

import os.path
from gamestate import *

# Private Attributes


class Player(object):

    # Class Attributes
    name = ""
    level = 1
    experience = 0
    attack = 10
    damage = 0

    def __init__(self, name__):
        self.name = name__

    def health(self):
        return 50 + (self.level * 50)

    def hitpoints(self):
        return self.health() - self.damage

    def printStats(self):
        # Line padding
        stats = "\n    "

        # Level: Name
        stats = stats + "%d: %s" % (self.level, self.name)
        
        # Hitpoints/Health
        stats = stats + "\t\t%d/%d\n" % (self.hitpoints(), self.health())

        print stats

    def load(self):
        success = False
        path = "players/%s.sav" % (self.name.lower())

        if os.path.exists(path):
            file = open(path, 'r')
            data = file.readline().split(':')

            if len(data) == 3:
                success = True
                self.level = int(data[0])
                self.experience = int(data[1])
                self.attack = int(data[2])

                print "Welcome back %s. Your progress has been restored." % (self.name)

            file.close()
        
        return success

    def save(self):
        if not os.path.exists("players/"):
            os.mkdir("players/")

        path = "players/%s.sav" % (self.name.lower())
        file = open(path, 'w')

        data = ":".join((str(self.level), str(self.experience), str(self.attack)))

        file.write(data)
        print "-- Player data saved --"
        file.close()
