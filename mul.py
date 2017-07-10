#!/usr/bin/python
import cgi
print "content-type: text/html"
print

print '<html>'
print '<head>'
print '<title>Welcome to cloudera</title>'
print '<script>'
print '''body {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  font-weight: 100;
  font-size: 12px;
  line-height: 30px;
  color: #777;
  background: #4CAF50;
}'''

print '</script>'
print '</head>'
print '<body bgcolor = #4CAF50>'
num_data = cgi.FormContent()['num_data'][0]

num_task = cgi.FormContent()['num_task'][0]

fh = open('idiot.txt','w+')
fh.write(num_data)
fh.write("\n")
fh.write(num_task)
fh.close()

############################### Name Node Part #################################

print ' <center><h1>For Name Node :</h1></center>'
print '<br>'
print "<form action='/scripts/mul_integrate.py'>"
      
print "<center>Enter the ip address: <input type = 'text' name = nam /></center>"   
print "<br>"  
     

print
print

########################### Job Tracker Part ############################

print ' <center><h1>For Job  Tracker :</h1></center>'
print '<br>'
print "<center>Enter the ip address: <input type = 'text' name = job /></center>"   
print "<br>"  
     

print
print
    
    
############################# Data Node Part #################################    
   
i=0   
print ' <center><h1>For Data Node :</h1></center>'
print '<br>'

while i < int(num_data):
        var1 = "num_data"+str(i)
        print "<center>Enter the ip address: <input type = 'text' name = var1 /></center>"   
        print "<br>"  
        i = i+1

print
print


###################### Task Tracker Part ##########################

j=0

print ' <center><h1>For Task Tracker :</h1></center>'
print '<br>'

while j < int(num_task):
        var2 = "num_task"+str(j)
        #print var2
        print "<center>Enter the ip address: <input type = 'text' name = var2 /></center>"
        print "<br>"
        j = j+1  


print
print       

############################ Client Part ################################

print ' <center><h1>For Client :</h1></center>'
print '<br>'
print "<center>Enter the ip address: <input type = 'text' name = client /></center>"   
print "<br>"  
     

print "<center><input type = 'submit' /></center>" 
print "</form>"  


print '</body>'
print '</html>'



