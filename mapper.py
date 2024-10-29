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

                # Temperatura maxima
                temperature = float(values[5])

                if -1.0 <= temperature <= 27.0:
                    continue

                nombreCiudad = filename.split("-")[2]
                print('Ciudad: %s %s \t%s' % (nombreCiudad, temperature, 1)) 