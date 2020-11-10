#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(" ", line)
    
    for i, word in enumerate(words):
    	if word == "\"GET":
        	print( words[i+1] + '\t' + "1")
