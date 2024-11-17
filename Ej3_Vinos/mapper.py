#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
    #user_number = ""
    type_wine = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0].split("-")[1]
    
    # Eliminar espacios
    line = line.strip()
    values = line.split(";")

    value_fixed_acidity = values[0]
    value_volatile_acidity  = values[1]
    value_citric_acid = values[2]
    value_residual_sugar = values[3]
    value_chlorides = values[4]
    value_free_sulfur_dioxide = values[5]
    value_total_sulfur_dioxide = values[6]
    value_density = values[7]
    value_pH = values[8]
    value_sulphates = values[9]
    value_alcohol = values[10]
    value_quality = values[11]

    print("%s:fixed_acidity\t%s" % (type_wine, value_fixed_acidity))
    print("%s:volatile_acidity\t%s" % (type_wine, value_volatile_acidity))
    print("%s:citric_acid\t%s" % (type_wine, value_citric_acid))
    print("%s:residual_sugar\t%s" % (type_wine, value_residual_sugar))
    print("%s:chlorides\t%s" % (type_wine, value_chlorides))
    print("%s:free_sulfur_dioxide\t%s" % (type_wine, value_free_sulfur_dioxide))
    print("%s:total_sulfur_dioxide\t%s" % (type_wine, value_total_sulfur_dioxide))
    print("%s:density\t%s" % (type_wine, value_density))
    print("%s:pH\t%s" % (type_wine, value_pH))
    print("%s:sulphates\t%s" % (type_wine, value_sulphates))
    print("%s:alcohol\t%s" % (type_wine, value_alcohol))
    print("%s:quality\t%s" % (type_wine, value_quality))
