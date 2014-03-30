#-------------------------------------------------------------------------------
# Name:        tools
# Purpose:
#
# Author:      Martin
#
# Created:     28/03/2014
# Copyright:   (c) Martin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import bisect
import itertools
import person
import csv


#found on http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/
def weighted_choice_b2(weights):
    partsums = list(itertools.accumulate(weights))
    total = partsums[-1]
    rnd = random.random() * total
    return bisect.bisect_right(partsums, rnd)

def generate_age(choices):
    total = sum(choices.values())
    pick = random.uniform(0, total)
    current = 0
    for key, value in choices.items():
        current += value
        if current > pick:
            return key

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)