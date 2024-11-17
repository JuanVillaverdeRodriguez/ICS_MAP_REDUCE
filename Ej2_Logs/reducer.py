#!/usr/bin/env python

import sys

first = True
real_max_count = 0
current_max_count = 0
real_max_string = ""
current_max_string = ""
mode = ""

# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    keys, current_count = line.split('\t', 1)
    mode, current_string = keys.split(':',1)
    current_count = int(current_count)

    if first:
        first = False
        real_max_count = current_count
        real_max_string = current_string
        current_max_string = current_string
        current_max_count = current_count
    else:
        if (current_string == current_max_string):
            current_max_count = current_max_count + current_count
        else:
            if (current_max_count >= real_max_count):
                real_max_count = current_max_count
                real_max_string = current_max_string
            current_max_string = current_string
            current_max_count = current_count


if (mode == "1"):
    print ('El usuario que mas visito paginas .ps fue %s visitando %s paginas.' % (real_max_string, real_max_count))
elif(mode == "2"): 
    print ('El lugar mas visitado fue %s con %s visitas' % (real_max_string, real_max_count))

