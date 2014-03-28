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


#found on http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/

def weighted_choice_b2(weights):
    partsums = list(itertools.accumulate(weights))
    total = partsums[-1]
    rnd = random.random() * total
    return bisect.bisect_right(partsums, rnd)
