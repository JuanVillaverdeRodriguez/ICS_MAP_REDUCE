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
                temperature = float(values[5])
                    
                # Aplica el filtro de temperatura
                if -1.0 <= temperature <= 27.0:
                    continue

                # Imprime el resultado en el formato esperado
                # print('%s\t%s' % (temperature, 1))  
                nombreCiudad = filename.split("-")[2]
                print('Ciudad: %s %s \t%s' % (nombreCiudad, temperature, 1)) 