#-------------------------------------------------------------------------------
# Name:        person
# Purpose:
#
# Author:      Martin
#
# Created:     28/03/2014
# Copyright:   (c) Martin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, random
import main, tools

POP_SIZE = 200

nameMale = []
nameFemale = []
nameLast = []
popList = []
probMale = []
probFemale = []
probLast = []
raceList = ["CAUCASIAN", "BLACK", "HISPANIC", "ASIAN"]

adults = []
elders = []
teens = []
children = []


def nameListGenerator():
    # Create name lists
    for line in open("male.first.txt"):
        info = line.split()
        nameMale.append(info[0])
        probMale.append(float(info[1]))

    for line in open("female.first.txt"):
        info = line.split()
        nameFemale.append(info[0])
        probFemale.append(float(info[1]))

    for line in open("last.txt"):
        info = line.split()
        nameLast.append(info[0])
        probLast.append(float(info[1]))


class Person:
    def __init__(self, first, last, age, sex, race):
        self.first = first
        self.last = last
        self.name = first + " " + last
        self.age = age
        if sex == 0:
            self.sex = "M"
        else:
            self.sex = "F"
        self.race = race

def storkify():
    global numMale
    global numFemale
    numMale = 0
    numFemale = 0
    for i in range(0, POP_SIZE):
        sex = random.randint(0,1)
        # decide if male or female, pick first name
        if sex == 0:
            index = int(tools.weighted_choice_b2(probMale))
            first = nameMale[index]
            numMale += 1
        elif sex == 1:
            index = int(tools.weighted_choice_b2(probFemale))
            first = nameFemale[index]
            numFemale += 1
        else:
            sys.exit("he-she?")

        # pick last name
        index = int(tools.weighted_choice_b2(probLast))
        last = nameLast[index]
        age = str(random.randint(1, 100))       # determine age (needs updating)
        race = random.choice(raceList)
        person = Person(first, last, age, sex, race)
        popList.append(person)
        age = int(age)
        if age < 13:                            # split age into groups
            children.append(person)
        elif age >= 13 and age < 20:
            teens.append(person)
        elif age >= 20 and age < 65:
            adults.append(person)
        else:
            elders.append(person)

def census():                                   # print out population info
    #ghetto table time
    results = open("censusResults.txt", "w")
    tableName = "NAME"
    tableRace = "RACE"
    #print("-" * 56)
    results.write("-" * 56 + "\n")
    #print("| " + tableName.center(25) + " | SEX | AGE | " + tableRace.center(13) + " |")
    results.write("| " + tableName.center(25) + " | SEX | AGE | "  + tableRace.center(13) + " |\n")
    #print("-" * 56)
    results.write("-" * 56 + "\n")
    for each in popList:
        #print("| " + each.name.center(25) + " | " + each.sex.center(3) + " | " +
        #str(each.age.center(3)) + " |")
        results.write("| " + each.name.center(25) + " | " + each.sex.center(3) + " | " +
        str(each.age.center(3)) + " | " + each.race.center(13) + " |\n")
        #print("-" * 56)
        results.write("-" * 56 + "\n")

def person():
    nameListGenerator()
    storkify()
    census()
