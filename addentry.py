#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb


print "content-type: text/html"
print
#print cgi.FormContent()

username = cgi.FormContent()['username'][0]
uemail = cgi.FormContent()['uemail'][0]
uname = cgi.FormContent()['u_name'][0]
upass = cgi.FormContent()['u_pass'][0]

'''
print uname
print upass
print username
print upass
'''
mariadb_connection = mariadb.connect(user='root', password='redhat', database='project')

cursor = mariadb_connection.cursor(buffered=True)



cursor.execute("insert into user_info values('{0}','{1}','{2}','{3}')".format(uname,upass,username,uemail))

mariadb_connection.commit()



print '<h1><center>Your details are :-</center></h1>'
print '<center> <h3>'
print "Name :    ",username
print '<br>'
print '<br>'
print '<br>'
print "email :    ",uemail
print '<br>'
print '<br>'
print '<br>'
print "User Name :    ",uname 
print '<br>'
print '<br>'
print '<br>'
print "Your account has been created successfully"
print '<br>'
print '<br>'
print '<br>'

