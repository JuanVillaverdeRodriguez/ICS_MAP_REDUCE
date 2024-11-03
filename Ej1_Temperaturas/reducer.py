#!/usr/bin/env python

import sys


current_max_temperature = 0
current_min_temperature = 0
current_town_name = ""
town_name = ""
first_temp = 0
last_temp = 0
first_town = None
last_town = None
first = True


# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    if first:
        first = False
        first_temp, first_town = line.split('\t', 1)
    else:
        last_temp, last_town = line.split('\t', 1)
    

    '''# parse the input we got from mapper.py
    temperature, town = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word'''

# do not forget to output the last word if needed!
print ('%s\t%s' % (first_temp, first_town))
print ('%s\t%s' % (last_temp, last_town))
