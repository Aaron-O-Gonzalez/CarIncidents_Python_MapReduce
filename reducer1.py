#!/usr/bin/env python3

import sys

current_vin = None
vin = None
make = None
year = None

def reset():
    current_vin =  None
    vin = None
    make = None
    year = None

def flush():
    print(f'{current_vin}\t{make}\t{year}')

for line in sys.stdin:
    line = line.strip()
    elements = line.split('\t')
    vin = elements[0]
    incident_type = elements[1]

    if vin == current_vin:
        if incident_type == 'I':
            make = elements[2]
            year = elements[3]

    elif vin!=current_vin:
        if current_vin != None:
            flush()
        reset()
    
    if incident_type == 'I':
        make = elements[2]
        year = elements[3]
    
    current_vin = vin

flush()


