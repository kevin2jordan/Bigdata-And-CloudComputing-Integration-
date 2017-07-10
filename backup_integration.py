#!/usr/bin/python

import commands,cgi

print "Content-type: text/html"
print 



################################  Name Node Configuration #############################

def configure_namenode(nameIp,masterIp,containerName):
	
        password="p"
	
        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker exec {2} mkdir -p /name".format(password,masterIp,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p /had_test".format(password,masterIp))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp {2}:/etc/hadoop/hdfs-site.xml /had_test".format(password,masterIp,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/hdfs-site.xml /project".format(password,masterIp))
        commands.getstatusoutput("sudo chown apache /project/hdfs-site.xml")


        fh=open('/project/hdfs-site.xml','a')
        writestring="<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/name</value>\n</property>\n</configuration>\n"
        fh.write(writestring)
        fh.close()


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /project/hdfs-site.xml {1}:/had_test".format(password,masterIp))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp /had_test/hdfs-site.xml {2}:/etc/hadoop".format(password,masterIp,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp {2}:/etc/hadoop/core-site.xml /had_test".format(password,masterIp,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/core-site.xml /project".format(password,masterIp))
        commands.getstatusoutput("sudo chown apache /project/core-site.xml")


        fh=open('/project/core-site.xml','a')
        writestring="<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n".format(nameIp)
        fh.write(writestring)   
        fh.close()

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /project/core-site.xml {1}:/had_test".format(password,masterIp))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp /had_test/core-site.xml {2}:/etc/hadoop".format(password,masterIp,containerName))

        commands.getstatusoutput("echo 'Y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker exec {2} hadoop namenode -format".format(password,masterIp,containerName))
        sign=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker exec {2} hadoop-daemon.sh start namenode".format(password,masterIp,containerName))
	
        if sign[0]==0:
	        print ""
        else:
	        print "Some error" + "\n"
############################## End Of NameNode Configuration ###########################


############################## Data Node Configuration ################################

def  configure_datanode(slaveIp,masterIp,containerName):
        
        password="p"
       

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} systemctl start docker".format(password,slaveIp))

        commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} lvcreate --size 2G --name {2} vgcloud".format(password,slaveIp,containerName))

        commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkfs.ext4 /dev/vgcloud/{2}".format(password,slaveIp,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p {2}".format(password,slaveIp,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mount /dev/vgcloud/{2} /{2}".format(password,slaveIp,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker run -dit --privileged=true -v /{2}:/data --name {2} cluster:v4".format(password,slaveIp,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p /had_test".format(password,slaveIp))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp {2}:/etc/hadoop/hdfs-site.xml /had_test".format(password,slaveIp,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/hdfs-site.xml /project".format(password,slaveIp))
        commands.getstatusoutput("sudo chown apache /project/hdfs-site.xml")


        fh=open('/project/hdfs-site.xml','a')
        writestring="<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n</configuration>\n"
        fh.write(writestring)
        fh.close()


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /project/hdfs-site.xml {1}:/had_test".format(password,slaveIp))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp /had_test/hdfs-site.xml {2}:/etc/hadoop".format(password,slaveIp,containerName))



        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp {2}:/etc/hadoop/core-site.xml /had_test".format(password,slaveIp,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/core-site.xml /project".format(password,slaveIp))
        commands.getstatusoutput("sudo chown apache /project/core-site.xml")


        fh=open('/project/core-site.xml','a')
        writestring="<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n".format(masterIp)
        fh.write(writestring)   
        fh.close()


        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /project/core-site.xml {1}:/had_test".format(password,slaveIp))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp /had_test/core-site.xml {2}:/etc/hadoop".format(password,slaveIp,containerName))

        
        sign=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker exec {2} hadoop-daemon.sh start datanode".format(password,slaveIp,containerName))
	



        if sign[0]==0:
	        print ""
        else:
	        print "Some error" + "\n"


#######################  End Of Date Node Configuration ##################################


#################### Configuration of Tasktracker ######################################
def configure_tasktracker(task_ip,job_ip,containerName):
       
        password="p"
        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} systemctl start docker".format(password,task_ip))
        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker run -dit --name {2} cluster:v6".format(password,task_ip,containerName))

        #local download of configurtaion file in had_test

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} mkdir -p /had_test".format(password,task_ip))

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker cp {2}:/etc/hadoop/mapred-site.xml /had_test".format(password,task_ip,containerName))

        #downloading files to server site

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/mapred-site.xml /project/".format(password,task_ip))

        # changing owner so that file can be modified

        commands.getstatusoutput("sudo chown apache  /project/mapred-site.xml")

        # chaning configuration file locally

        fh1=open('/project/mapred-site.xml','a')

        writestring="<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n".format(job_ip)

        fh1.write(writestring)
        fh1.close()


        #copying files to main server base 
      

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no  /project/mapred-site.xml  {1}:/had_test/".format(password,task_ip))

        cmd2= "sudo sshpass -p {0} ssh {1} docker cp /had_test/mapred-site.xml {2}:/etc/hadoop/mapred-site.xml".format(password,task_ip,containerName) 


        #sign=commands.getstatusoutput(cmd1)
        sign=commands.getstatusoutput(cmd2)


        #execting the hadoop jobtracker services
        sign=commands.getstatusoutput("sudo sshpass -p  {0} ssh {1} docker exec {2} hadoop-daemon.sh start tasktracker".format(password,task_ip,containerName))
	

        if sign[0]==0:
	        print ""
        else:
	        print "Some error" + "\n"
	        
	        
#######################   End Of Tasktracker Configuration ##############################



##################### JobTracker Configuration #######################################

def configure_jobtracker(masterIp,jobIp,Ip,containerName):
       
        password="p"
        #containerName
      

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} mkdir -p /had_test".format(password,Ip))

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker cp {2}:/etc/hadoop/core-site.xml /had_test".format(password,Ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker cp {2}:/etc/hadoop/mapred-site.xml /had_test".format(password,Ip,containerName))

        #downloading files to server site

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/core-site.xml /project/".format(password,Ip))
        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/mapred-site.xml /project/".format(password,Ip))

        # changing owner so that file can be modified

        commands.getstatusoutput("sudo chown apache  /project/mapred-site.xml")
        commands.getstatusoutput("sudo chown apache  /project/core-site.xml")

        # chaning configuration file locally

        fh1=open('/project/mapred-site.xml','a')

        writestring="<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n".format(jobIp)

        fh1.write(writestring)
        fh1.close()


        fh2=open('/project/core-site.xml','a')
        str2 = "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n".format(masterIp)


        fh2.write(str2)

        fh2.close()

        #copying files to main server base 
        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no  /project/core-site.xml {1}:/had_test/".format(password,Ip))

        commands.getstatusoutput("sshpass -p {0} sudo scp -o stricthostkeychecking=no  /project/mapred-site.xml {1}:/had_test/".format(password,Ip))

        cmd1= "sudo sshpass -p {0} ssh {1} docker cp /had_test/core-site.xml {2}:/etc/hadoop/".format(password,Ip,containerName) 
        cmd2= "sudo sshpass -p {0} ssh {1} docker cp /had_test/mapred-site.xml {2}:/etc/hadoop/".format(password,Ip,containerName) 


        sign=commands.getstatusoutput(cmd1)
        sign=commands.getstatusoutput(cmd2)


        #execting the hadoop jobtracker services
        sign=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker exec {2} hadoop-daemon.sh start jobtracker".format(password,Ip,containerName))
	

        if sign[0]==0:
	        print ""
        else:
	        print "Some error" + "\n"
	        
	        
#####################  End of JobTracker Configuration ###########################
	        
##############################  Client COnfiguration ###########################



        
def configure_client(Ip,masterIp,jobIp,containerName):
        password='p'
        
        fh=open('oppy.txt','w')
        fh.write(Ip)
        fh.close()
  
        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} systemctl start docker".format(password,Ip))
          
        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker run -dit --privileged=true --name {2} cluster:v5".format(password,Ip,containerName))
        
        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} mkdir -p /had_test".format(password,Ip))

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker cp {2}:/etc/hadoop/core-site.xml /had_test".format(password,Ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker cp {2}:/etc/hadoop/mapred-site.xml /had_test".format(password,Ip,containerName))

        #downloading files to server site

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/core-site.xml /project/".format(password,Ip))
        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/mapred-site.xml /project/".format(password,Ip))

        # changing owner so that file can be modified

        commands.getstatusoutput("sudo chown apache  /project/mapred-site.xml")
        commands.getstatusoutput("sudo chown apache  /project/core-site.xml")

        # chaning configuration file locally

        fh1=open('/project/mapred-site.xml','a')

        writestring="<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n".format(jobIp)

        fh1.write(writestring)
        fh1.close()


        fh2=open('/project/core-site.xml','a')
        str2 = "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n".format(masterIp)


        fh2.write(str2)

        fh2.close()

        #copying files to main server base 
        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no  /project/core-site.xml {1}:/had_test/".format(password,Ip))

        commands.getstatusoutput("sshpass -p {0} sudo scp -o stricthostkeychecking=no  /project/mapred-site.xml {1}:/had_test/".format(password,Ip))

        cmd1= "sudo sshpass -p {0} ssh {1} docker cp /had_test/core-site.xml {2}:/etc/hadoop/".format(password,Ip,containerName) 
        cmd2= "sudo sshpass -p {0} ssh {1} docker cp /had_test/mapred-site.xml {2}:/etc/hadoop/".format(password,Ip,containerName) 


        sign=commands.getstatusoutput(cmd1)
        sign=commands.getstatusoutput(cmd2)
	
        if sign[0]==0:
	        print ""
        else:
	        print "Some error" + "\n"
	       
	        	        
###########################################################################

def configure_common(ip,name_ip,job_ip,containerName):
        password="p"
        
        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} systemctl start docker".format(password,ip))

        commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} lvcreate --size 2G --name {2} vgcloud".format(password,ip,containerName))

        commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkfs.ext4 /dev/vgcloud/{2}".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p {2}".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mount /dev/vgcloud/{2} /{2}".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker run -dit --privileged=true -v /{2}:/data --name {2} cluster:v7".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker exec {2} mkdir -p /data".format(password,ip,containerName))


        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p /had_test".format(password,ip))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp {2}:/etc/hadoop/hdfs-site.xml /had_test".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/hdfs-site.xml /project".format(password,ip))
        commands.getstatusoutput("sudo chown apache /project/hdfs-site.xml")

        fh=open('/project/hdfs-site.xml','a')
        writestring="<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n</configuration>\n"
        fh.write(writestring)
        fh.close()

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /project/hdfs-site.xml {1}:/had_test".format(password,ip))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp /had_test/hdfs-site.xml {2}:/etc/hadoop".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp {2}:/etc/hadoop/core-site.xml /had_test".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/core-site.xml /project".format(password,ip))
        
        commands.getstatusoutput("sudo chown apache /project/core-site.xml")

        fh=open('/project/core-site.xml','a')
        writestring="<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:10001</value>\n</property>\n</configuration>\n".format(name_ip)
        fh.write(writestring)   
        fh.close()

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /project/core-site.xml {1}:/had_test".format(password,ip))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker cp /had_test/core-site.xml {2}:/etc/hadoop".format(password,ip,containerName))
	
        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker cp {2}:/etc/hadoop/mapred-site.xml /had_test".format(password,ip,containerName))

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no {1}:/had_test/mapred-site.xml /project/".format(password,ip))

        commands.getstatusoutput("sudo chown apache  /project/mapred-site.xml")

        fh1=open('/project/mapred-site.xml','a')

        writestring="<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9001</value>\n</property>\n</configuration>\n".format(job_ip)

        fh1.write(writestring)
        fh1.close()

        commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no  /project/mapred-site.xml  {1}:/had_test/".format(password,ip))

        cmd2= "sudo sshpass -p {0} ssh {1} docker cp /had_test/mapred-site.xml {2}:/etc/hadoop/mapred-site.xml".format(password,ip,containerName) 
        
        sign=commands.getstatusoutput(cmd2)
        
        sign=commands.getstatusoutput("sudo sshpass -p  {0} ssh {1} docker exec {2} hadoop-daemon.sh start tasktracker".format(password,ip,containerName))

        
        sign=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker exec {2} hadoop-daemon.sh start datanode".format(password,ip,containerName))




        if sign[0]==0:
	        print ""
        else:
	        print "Some error" + "\n"
        



##################################  Main Part ################################

      



no_data_node=cgi.FormContent()['data_node'][0]
no_task_tracker=cgi.FormContent()['task_tracker'][0]

no_data_node=int(no_data_node)
no_task_tracker=int(no_task_tracker)

minm=8000000
maxm=0
if no_data_node <= no_task_tracker:
        minm=no_data_node
        maxm=no_task_tracker
else:
        minm=no_task_tracker
        maxm=no_data_node

lines = open('hdfs_unused.txt').readlines()

maxm=maxm+2
minm=minm+2
open('hdfs_unused.txt', 'w').writelines(lines[maxm+1:])
open('hdfs_used.txt', 'a').writelines(lines[0:maxm+1])

ipaddr = open('hdfs_used.txt','r').readlines()

name_ip='a'
job_ip='a'
i=0
j=0
k=0
var=0

##########################       Driver Programm          ###############################
      
while var<minm:
        if var==0:
        
                ip= ipaddr[var].rstrip()
                
                commands.getstatusoutput("sudo sshpass -p 'p' ssh -o stricthostkeychecking=no {0} systemctl start docker".format(ip))
                cmd = "sudo sshpass -p 'p' ssh {0} docker run -dit --name name{1} cluster:v4".format(ip,i)
                commands.getstatusoutput(cmd)
                
                name_ip = commands.getstatusoutput("sudo sshpass -p 'p' ssh {0} docker inspect name{1} | jq '.[].NetworkSettings.Networks.bridge.IPAddress' ".format(ip,i))
                name_ip=name_ip[1].strip('"')
                
               
	        configure_namenode(name_ip,ip,"name"+str(i))
		i=i+1
		
		
	elif var==1:
                ip= ipaddr[var].rstrip()
                commands.getstatusoutput("sudo sshpass -p 'p' ssh -o stricthostkeychecking=no {0} systemctl start docker".format(ip))
                cmd = "sudo sshpass -p 'p' ssh {0} docker run -dit --name job{1} cluster:v5".format(ip,j)
                commands.getstatusoutput(cmd)
                
                job_ip = commands.getstatusoutput("sudo sshpass -p 'p' ssh {0} docker inspect job{1} | jq '.[].NetworkSettings.Networks.bridge.IPAddress' ".format(ip,j))
                job_ip = job_ip[1].strip('"')
                
                configure_jobtracker(name_ip,job_ip,ip,"job"+str(j))
		j=j+1
		
	else:
	        ip= ipaddr[var].rstrip()
	        configure_common(ip,name_ip,job_ip,"common"+str(k))
		k=k+1 
		      
        var = var+1
        
      

if maxm==no_task_tracker+2:
        while var<maxm:
                ip= ipaddr[var].rstrip()
                configure_tasktracker(ip,job_ip,"task"+str(k))
		k=k+1 
		var=var+1
		
if maxm==no_data_node+2:
        while var<maxm:
                ip= ipaddr[var].rstrip()
                configure_datanode(ip,name_ip,"data"+str(k))
		k=k+1 
		var=var+1

	
ip= ipaddr[var].rstrip()
                	
configure_client(ip,name_ip,job_ip,"client")

print '<h1><center>Your cluster has been created successfully :-</center></h1>'
print '<center> <h3>'
print "Number of Name node :    1" 
print '<br>'
print '<br>'
print '<br>'
print "Number of Data node :    ",no_data_node
print '<br>'
print '<br>'
print '<br>'
print "Number of Job  Tracker :    1"
print '<br>'
print '<br>'
print '<br>'

print "Number of Task Tracker  :    ",no_task_tracker 
print '<br>'
print '<br>'
print '<br>'
print "<a href = http://www.pxp.com/show_user.html>click here to go to Menu Bar</a>"
print '<br>'
print '<br>'
print '<br>'





