#!/usr/bin/env python

import sys

current_key = ""
adder = 0
counter = 0
first = True

# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    key, value = line.split('\t', 1)
    #type_wine, type_value = keys.split(':',1)

    try:
        value = float(value)
    except ValueError:
        exit(1)
    
    if (first):
        current_key = key
        first = False

    if (current_key == key):
        adder += value
        counter += 1
    else:
        average = adder / counter
        print("La media de valores de %s es: %f" % (current_key, average))

        current_key = key
        counter = 0
        adder = 0

        adder += value
        counter += 1

average = adder / counter
print("La media de valores de %s es: %f" % (current_key, average))
