#!/usr/bin/python

import sys
import re

previous = None
sum = 0
total = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print previous + '\t' + str(sum/total)
        previous = key
        sum = 0
        total = 0
        
    #in case the mass is not empty
    if value != '\n':
    	sum = sum + float(value)
    
    total = total + 1

print previous + '\t' + str(sum/total)
