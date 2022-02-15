#!/usr/bin/env python3
import sys

accidents = {}

for line in sys.stdin:
    line = line.strip()
    elements = line.split('\t')
    make = elements[1]
    year = elements[2]
    count = int(elements[3])
    key = make + '\t' + year
    
    if key not in accidents:
        accidents[key] = 1
    else:
        accidents[key] += 1

for keys in accidents.keys():
    print(keys + '\t' + str(accidents[keys]))



