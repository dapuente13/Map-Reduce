#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(",", line)
    date = re.split("-", words[0])
    print( date[0] + "\t" + words[4])
