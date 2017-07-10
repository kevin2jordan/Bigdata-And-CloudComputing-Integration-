#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb


print "content-type: text/html"
print

u_name=cgi.FormContent()['uname'][0]
paswd=cgi.FormContent()['upass'][0]

mariadb_connection = mariadb.connect(user='root', password='redhat', database='project')

cursor = mariadb_connection.cursor(buffered=True)

cursor.execute("select upass from user_info where uname='{0}'".format(u_name))
passwd=cursor.fetchone()[0]
#print '<head><meta http-equiv="refresh" content="5;url=http://www.cloudera.com/show_user.html"/></head>'
passwd=str(passwd)
if passwd==paswd:
        print '<head><meta http-equiv="refresh" content="1;url=http://www.pxp.com/show_user.html"/></head>'
        		
else :
  	print '<head><meta http-equiv="refresh" content="1;url=http://www.pxp.com/login_valid.html"/></head>'



