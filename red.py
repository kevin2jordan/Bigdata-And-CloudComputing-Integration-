#!/usr/bin/python

import sys
ans=0
tmp="0"

for var in sys.stdin:
        var=var.strip()
        var=var.split(',')
        tmp1=float(var[0])
        tmp2=float(var[1])
        if tmp2>float(tmp):
                ans=tmp1
                tmp=tmp2
                
ans = int(ans)             
print "The next employee will left job whose employee ID is " + str(ans)              
