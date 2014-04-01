#-------------------------------------------------------------------------------
# Name:        resources
# Purpose:
#
# Author:      Martin
#
# Created:     01/04/2014
# Copyright:   (c) Martin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Resource:

    def __init__(self, name, renewable, rate, cap, amount):
        self.name = name
        self.renewable = renewable
        self.rate = rate
        self.cap = cap
        self.amount = amount
        self.available = True

    def isAvailable(self):
        return self.available

    def harvest(self, amount):
        if self.available:  #if there is atleast 1 available
            if self.amount - amount < 0:
                #amount requested not available, harvest all available
                #ie 10 requested, only 8 available, return 8
                amount = self.amount
                self.amount = 0
                #return amount
            else:
                self.amount -= amount
            if self.amount == 0:
                self.available = False
            return amount
        else:
            return False

    def renew(self):
        #runs once per 'tick'
        if self.available == False:
            self.available

        #doesn't exceed cap
        if self.amount + self.rate <= cap:
            self.amount += self.rate
        else:
            self.amount = cap