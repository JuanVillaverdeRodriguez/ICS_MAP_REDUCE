#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
    #user_number = ""
    user_number = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0]
    #town_name = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0][3:]
    
    # Eliminar espacios
    line = line.strip()
    values = line.split()

    machine_name = values[0]
    timestamp = values[1]
    user_id = values[2]
    url = values[3].strip('\"')
    size = values[4]
    retrieval_time = values[5]

    ps = False

    urlps = url.split('.')
    urlLen = len(urlps)
    if (urlps[urlLen-1] == "ps" or urlps[urlLen-2] == "ps"):
        ps = True
        
    if (ps):
        print("1:%s\t%s" % (user_number, 1))
    print("2:%s\t%s" % (url, 1))
    

