#!/usr/bin/python

import cgi
print "content-type: text/html"
#print "location: ../form.html"
#print

#print cgi.FormContent()

userName = cgi.FormContent()['username'][0]
passWord = cgi.FormContent()['password'][0]

#print userName
#print passWord
suser = "rahul"
spass = "mitnickkevin"

if suser == userName  and spass == passWord : 
        print "location: ../form.html"
        print
else : 
        print "location: ../login.html"
        print   
           
        
print "hello"
