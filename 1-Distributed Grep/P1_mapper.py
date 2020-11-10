#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(" ", line)
    arg = sys.argv[1]
    for w in words:
    	if w == arg:
    		print( w.lower() + "\t" + line)
