#!/usr/bin/python2

import cgi, cgitb ,os,webbrowser
import mysql.connector as mariadb
form = cgi.FieldStorage()

print "Content-type: text/html"
print

print '<html>'
print '<head>'
print '<title>checking validity</title>'

print '</head>'
print '<body>'

u_name=form.getvalue('uname')
paswd=form.getvalue('psw')

mariadb_connection = mariadb.connect(user='root', password='redhat', database='project')

cursor = mariadb_connection.cursor(buffered=True)
cursor.execute("select Password from user_entry where ID='{0}'".format(u_name))
passwd=cursor.fetchone()[0]
passwd=str(passwd)
if passwd==paswd:
	print '<center>'
        print '<h1 style="color:red">login successfully</h1>'
        print '</center>'
		
else :
  	print "Wrong Credentials"

print '</body>'
print '</html>'


