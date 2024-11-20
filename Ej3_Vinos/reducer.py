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

    # red:fixed_acidity
    # red:volatile_acidity
    # white:fixed_acidity
    # white:volatile_acidity
    
    try:
        value = float(value)
    except ValueError:
        continue
    
    if (first):
        current_key = key
        first = False

    if (current_key != key):
   
        average = adder / counter
        print("La media de valores de %s es: %f" % (current_key, average))

        current_key = key
        counter = 0
        adder = 0

    adder += value
    counter += 1
    
if (counter != 0):
    average = adder / counter
    print("La media de valores de %s es: %f" % (current_key, average))
