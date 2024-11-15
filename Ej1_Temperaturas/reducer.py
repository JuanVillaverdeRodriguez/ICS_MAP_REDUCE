#!/usr/bin/env python

import sys

first = True
mode = ""
places = ""
temp = ""
count = 0


# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    keys, new_place = line.split('\t', 1)
    new_mode, new_temp = keys.split(':',1)

    if first:
        first = False
        mode = new_mode
        temp = new_temp
        places = new_place 
    else:
        if (mode == "Max"):
            if (new_temp == temp):
                count = count + 1
                places = places + ", " + new_place
        elif (mode == "Min"):
            if (new_temp != temp):
                places = new_place
                temp = new_temp
                count = 0
            else:
                count = count + 1
                places = places + ", " + new_place

if (mode == "Max"):
    if (count == 0):
        print ('El lugar con mas calor fue %s con %s grados' % (places, temp))
    else:
        print ('Los lugares con mas calor fueron %s con %s grados' % (places, temp))
else: 
    if (count == 0):
        print ('El lugar mas frio fue %s con %s grados' % (places, temp))
    else:
        print ('Los lugares mas frio fueron %s con %s grados' % (places, temp))

