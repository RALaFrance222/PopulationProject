#-------------------------------------------------------------------------------
# Name:        personality
# Purpose:
#
# Author:      Martin
#
# Created:     29/03/2014
# Copyright:   (c) Martin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

class Personality:

    def __init__(self):
        self.chooseInterests()

    def chooseInterests(self):
        interests = []
        self.likes = []
        self.dislikes = []

        for line in open("data/interests.txt"):
            line = line.rstrip()
            interests.append(line)

        for i in range(0,3):
            # choose a like
            choice = random.choice(interests)
            self.likes.append(choice)
            interests.remove(choice)
            # choose a dislike
            choice = random.choice(interests)
            self.dislikes.append(choice)
            interests.remove(choice)

