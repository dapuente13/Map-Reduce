#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split("\t", line)
    
    if float(words[1]) <= 1: print("Range 1" + "\t" + words[0])
    elif float(words[1]) <= 2 and float(words[1]) > 1: print ("Range 2" + "\t" + words[0])
    elif float(words[1]) <= 3 and float(words[1]) > 2: print ("Range 3" + "\t" + words[0])
    elif float(words[1]) <= 4 and float(words[1]) > 3: print ("Range 4" + "\t" + words[0])
    elif float(words[1]) <= 5 and float(words[1]) > 4: print ("Range 5" + "\t" + words[0])
