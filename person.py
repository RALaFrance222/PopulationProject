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

import sys, random, csv
import main, tools, personality

POP_SIZE = 200

nameMale = []
nameFemale = []
nameLast = []
popList = []
probMale = []
probFemale = []
probLast = []
raceList = ["CAUCASIAN", "BLACK", "HISPANIC", "ASIAN"]
ageWeights = {"children": 22, "youngAdults": 24, "adults": 42, "elders": 10,
              "extraElderly": 2}

adults = []
elders = []
youngAdults =[]
children = []
extraElderly = []


def nameListGenerator():
    # Create name lists
    for line in open("data/male.first.txt"):
        info = line.split()
        nameMale.append(info[0])
        probMale.append(float(info[1]))

    for line in open("data/female.first.txt"):
        info = line.split()
        nameFemale.append(info[0])
        probFemale.append(float(info[1]))

    for line in open("data/last.txt"):
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
        chooseInterests(self)

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

def storkify():
    global numMale
    global numFemale
    global ages
    ages = [0,0,0,0]
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
        age = tools.generate_age(ageWeights)      # determine age

        if age == "children":
            age = random.randint(0, 15)
            ages[0] += 1
        elif age == "youngAdults":
            age = random.randint(16, 29)
            ages[1] += 1
        elif age == "adults":
            age = random.randint(30, 64)
            ages[2] += 1
        elif age == "elders":
            age = random.randint(65, 79)
            ages[3] += 1
        else:
            age = random.randint(80, 100)
            ages[3] += 1
        #age = str(age)
        race = random.choice(raceList)
        person = Person(first, last, age, sex, race)
        popList.append(person)

def census(sortby):
    if sortby == 1:
        popList.sort(key = lambda x: x.last)
    elif sortby == 2:
        popList.sort(key = lambda x: x.first)
    elif sortby == 3:
        popList.sort(key = lambda x: x.age)
    elif sortby == 4:
        popList.sort(key = lambda x: x.sex)

    out = "data/census.csv"
    data = ["Last, First, Sex, Age, Race".split(',')]
    for each in popList:
        info = "%s,%s,%s,%s,%s" % (each.last, each.first, each.sex, str(each.age), each.race)
        info = info.split(",")
        data.append(info)
    tools.csv_writer(data, out)


def person(sortby):
    nameListGenerator()
    storkify()
    census(sortby)
