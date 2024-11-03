#coding=utf-8
#!/usr/bin/env python

import sys

# Abre y procesa cada archivo línea por línea
for line in sys.stdin:
    # Eliminar espacios
    line = line.strip()
    values = line.split()

    # Extrae la temperatura (en este caso, asumimos que está en la posición 5)
    max_temperature = float(values[5])
    min_temperature = float(values[6])
    
    town_name = values[0]
    # Aplica el filtro de temperatura
    if max_temperature >= 27.0:
        print("%s\t%s" % (max_temperature, town_name))
    if (min_temperature <= -1.0) and (min_temperature >= -273.15):
        print("%s\t%s" % (min_temperature, town_name))
               	
                
                
                
