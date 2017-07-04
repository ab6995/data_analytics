# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:32:09 2017

@author: ashishbansal
"""

#!/usr/bin/env python
import sys 
for line in sys.stdin:
    line = line.decode('ascii','ignore')
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s \t %s' % (word,1))
        