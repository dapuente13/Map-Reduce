#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(",", line)
    
    #if type has ',' then it starts with '"' 
    if words[3][0] == '\"':
    	words[3] = words[3]+words[4] #concatenate words
    	words[3] = re.sub(r'\"','' ,words[3]) #remove "" from the type
    	print(words[3] + "\t" + words[5])
    
    else: print(words[3] + "\t" + words[4])
