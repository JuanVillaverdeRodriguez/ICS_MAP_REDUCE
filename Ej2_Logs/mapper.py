#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
    #town_name = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0][3:]

    # Eliminar espacios
    line = line.strip()
    values = line.split()

    machine_name = values[0]
    timestamp = values[1]
    user_id = values[2]
    url = values[3]
    size = values[4]
    retrieval_time = values[5]

    print("Machine name: %s" % machine_name)
    print("Timestamp: %s" % timestamp)
    print("User id: %s" % user_id)
    print("URL: %s" % url)
    print("Size: %s" % size)
    print("Retrieval time: %s" % retrieval_time)
    print("----------------------------------------------------")

