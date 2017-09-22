#!/usr/bin/env python
import sys
 
# maps words to their counts
count = 0
total = 0
for line in sys.stdin:
	total = total + 1
	line = line.strip()
	if int(line) == 1:
		count = count + 1
print (count*100)/total
