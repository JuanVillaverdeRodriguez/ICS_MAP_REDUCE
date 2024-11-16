#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
    town_name = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0][3:]

    # Eliminar espacios
    line = line.strip()
    values = line.split()

    # Extrae la temperatura (en este caso, asumimos que esta en la posicion 5)
    max_temperature = float(values[5])
    min_temperature = float(values[6])
    
    # town_name = line.split("-")[2].split(".")[0]
    # Aplica el filtro de temperatura
    if max_temperature >= 27.0:
        print("Max:%s\t%s" % (max_temperature, town_name))
    if (min_temperature <= -1.0) and (min_temperature >= -273.15):
        print("Min:%s\t%s" % (min_temperature, town_name))
                   
                
                
