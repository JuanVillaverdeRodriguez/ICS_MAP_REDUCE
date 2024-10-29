#!/usr/bin/env python
import os
import sys

# Ruta de la carpeta con los archivos de temperatura
folder_path = './TEMPERATURAS'

# Recorre cada archivo .txt en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # Abre y procesa cada archivo línea por línea
        with open(file_path, 'r') as file:
            for line in file:
                # Eliminar espacios
                line = line.strip()
                values = line.split()

                # Extrae la temperatura (en este caso, asumimos que está en la posición 5)
                max_temperature = float(values[5])
                min_temperature = float(values[6])
                
                town_name = filename.split("-")[2].split(".")[0]
                # Aplica el filtro de temperatura
                if max_temperature >= 27.0:
                	print("%s\t%s" % (max_temperature, town_name))
                if (min_temperature <= -1.0) or (min_temperature >= -273.15):
                	print("%s\t%s" % (min_temperature, town_name))
               	
                
                
                
