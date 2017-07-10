#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb
import commands

print "content-type: text/html"
print

Ipaddr=cgi.FormContent()['ipaddr'][0]
Ipaddr=Ipaddr.strip()
password='p'
commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p /hado2".format(password,Ipaddr))

commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} lvcreate --name hado2 --size 2G vgcloud".format(password,Ipaddr))
commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkfs.ext4 /dev/vgcloud/hado2".format(password,Ipaddr))
commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mount /dev/vgcloud/hado2 /hado2".format(password,Ipaddr))
cmd="sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker run -dit --name hadoo2 --privileged=true -v /hado2:/store1 final_hadoop2:v1".format(password,Ipaddr)
commands.getstatusoutput(cmd)

print "<br>"
print "<br>"
print "<br>"
print '<h1><center>Your cluster has been created successfully :-</center></h1>'
print "<br>"
print "<br>"
print "<br>"
print "<a href = http://www.pxp.com/show_user.html><center>click here to go to Menu Bar</center></a>"
