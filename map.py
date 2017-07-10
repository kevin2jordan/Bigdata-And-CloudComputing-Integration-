#!/usr/bin/python2

import sys

for var in sys.stdin:
        var=var.strip()
        var=var.split(',')
        data1=float(var[1])+float(var[4])+float(var[8])
        if var[10]=="low":
                data1=data1+0
        elif var[10]=="medium":
                data1=data1+1
        elif var[10]=="high":
                data1=data1+2
        data1=data1/4
        print str(var[0])+","+str(data1)
