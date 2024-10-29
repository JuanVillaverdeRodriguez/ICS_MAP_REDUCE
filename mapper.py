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
                # Elimina espacios en blanco al inicio y al final
                line = line.strip()
                
                # Divide la línea en valores
                values = line.split()

                # Extrae la temperatura (en este caso, asumimos que está en la posición 5)
                max_temperature = float(values[5])
                min_temperature = float(values[6])
                
                # Aplica el filtro de temperatura
                if max_temperature <= 27.0:
                	max_temperature = None
                if (min_temperature > -1.0) or (min_temperature <= -273.15):
                	min_temperature = None
               	if min_temperature == None and max_temperature == None:
               		continue
 

                # Imprime el resultado en el formato esperado
                # print('%s\t%s' % (temperature, 1))  
                nombreCiudad = filename.split("-")[2].split(".")[0]
                print('%s\t\t\t%s\t%s\t%s' % (nombreCiudad, max_temperature, min_temperature, 1)) 
