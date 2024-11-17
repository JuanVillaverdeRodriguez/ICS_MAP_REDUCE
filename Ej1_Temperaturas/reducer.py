#!/usr/bin/env python

import sys

first = True
mode = ""
places = ""
temp = ""
count = 1


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
        if (new_temp == temp):
            count = count + 1
            places = places + ", " + new_place

if (mode == "Max"):
    if (count == 1):
        print ('El lugar con mas calor fue %s con %s grados' % (places, temp))
    else:
        print ('Los lugares con mas calor fueron %s con %s grados' % (places, temp))
elif (mode == "Min"): 
    if (count == 1):
        print ('El lugar mas frio fue %s con -%s grados' % (places, temp))
    else:
        print ('Los lugares mas frio fueron %s con -%s grados' % (places, temp))

