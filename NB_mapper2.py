#!/usr/bin/env python
import sys
import math

clas = open('classes.txt','r')
cla=dict()
for i in clas.readlines():
    cla.update(eval(i))

m = 1
w = 1050054
count = 0
total = 0
total_no_class = 0
for i in cla:
    total_no_class = total_no_class + cla[i][0]
for line in sys.stdin:
	line = line.strip()
	test = eval(line)
	for i in test:
    		max_prob = -2147483647
    		max_class = ""
    		for c in cla:
        		prob = math.log(float(cla[c][1])/ (total_no_class+1))
        		for word in test[i]:
            			j = 1
				if c in eval(test[i][word]):
                			j = j + int(eval(test[i][word])[c])
	       			prob = prob + math.log((float(j)+float(m))/(cla[c][1]+ w))
        		if prob > max_prob:
            			max_prob = prob
            			max_class = c
    	if max_class in i[len(i.split(' ')[0])+1:].split(','):
        	print "1"
    	else:
		print "0"
