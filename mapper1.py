#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    elements = line.split(',')
    print(f'{elements[2]}\t{elements[1]}\t{elements[3]}\t{elements[5]}')
    