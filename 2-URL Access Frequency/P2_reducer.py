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
            print previous + '\t' + str(sum)
        previous = key
        sum = 0
        
    sum = sum + int(value)

print previous + '\t' + str(sum)
