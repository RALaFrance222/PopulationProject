#-------------------------------------------------------------------------------
# Name:        community
# Purpose:      provide basic code fooor the creation and utilization of communities
#
# Author:      Andrew LaFrance
#
# Created:     28/03/2014
# Copyright:   (c) Andrew 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, random, csv
import person, tools
from enum import Enum

#class Focus(Enum):
#    fishing = 0
#    hunting = 1
#    farming = 2
#    smithing = 3
#Using enumerators for the community's focus would be smart, i think, but not necessary for initial testing ~A    

focuses = ["fishing", "hunting", "farming", "smithing"]
POP_SIZE  = 100

class Community:
    
    def __init__(self, name = "Defaultia", focus = "fishing", popSize = POP_SIZE):
        self.name = name
        self.focus = focus #sets the primary focus/export of the village
        self.popSize = popSize
        self.popList = person.storkify(popSize)
        
    def addMember(self, addCount = 1):
        self.popList.extend(person.storkify(addCount))
        
    def census(self, sortby):
        if sortby == 1:
            self.popList.sort(key = lambda x: x.last)
        elif sortby == 2:
            self.popList.sort(key = lambda x: x.first)
        elif sortby == 3:
            self.popList.sort(key = lambda x: x.age)
        elif sortby == 4:
            self.popList.sort(key = lambda x: x.sex)
    
        out = "data/" + self.name + "census.csv"
        data = ["Name, Focus, popSize".split(',')]
        data.append([self.name, self.focus, self.popSize])
        data.append(["Last, First, Sex, Age, Race".split(',')])
        for each in self.popList:
            info = "%s,%s,%s,%s,%s" % (each.last, each.first, each.sex, str(each.age), each.race)
            info = info.split(",")
            data.append(info)
        tools.csv_writer(data, out)    
    
def communify(sortby):
    town = Community()
    town.census(sortby)
    