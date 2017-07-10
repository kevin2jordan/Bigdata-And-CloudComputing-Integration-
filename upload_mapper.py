#!/usr/bin/python2


import cgi
import commands

print "content-type:  text/html"
print


fdata=cgi.FormContent()['fname'][0]

fh=open('/webcontent/scripts/uploads/map.py' , 'w')
fh.write(fdata)
fh.close()

fi  = open('oppy.txt')
ip = fi.readlines()
ip=ip[0]
ip=ip.strip()

commands.getstatusoutput('sudo sshpass -p p scp /webcontent/scripts/uploads/map.py {0}:/had_test/'.format(ip))
commands.getstatusoutput("sudo sshpass -p p ssh -o stricthostkeychecking=no {0} docker cp /had_test/map.py client:/".format(ip))

print '<body bgcolor  = #4CAF50>'
print '<br>'
print '<br>'
print '<br>'
print '<br>'
print '<br>'
print '<br>'
print '<br>'
print '<br>'
print '<br>'

print '<center>'
print "<form  enctype='multipart/form-data' action='/scripts/upload_reducer.py' method='POST'>"
print "upload reducer files :<input  type='file'  name = 'fname'>"
print '</br>'
print '</br>'
print '</br>'
print "<input type = 'submit' />"
print '</form>'
print '</center>'
print '</body>'
