#!/usr/bin/python

import commands,cgi

print "Content-type: text/html"
print 

#print "Hellllooooo"
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
	        print("Your namenode is successfully configured...")
        else:
	        print("Some error")
############################## End Of NameNode Configuration ###########################


############################## Data Node Configuration ################################

def  configure_datanode(slaveIp,masterIp,containerName):
        
        password="p"
       

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker exec {2} mkdir -p /data".format(password,slaveIp,containerName))



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



        commands.getstatusoutput("echo 'Y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker exec {2} hadoop namenode -format".format(password,slaveIp,containerName))
        sign=commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker exec {2} hadoop-daemon.sh start datanode".format(password,slaveIp,containerName))
	



        if sign[0]==0:
	        print("Your datanode is successfully configured...")
        else:
	        print("Some error")


#######################  End Of Date Node Configuration ##################################


#################### Configuration of Tasktracker ######################################
def configure_tasktracker(task_ip,job_ip,containerName):
       
        password='p'

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
	        print("Your Tasktracker is successfully configured...")
        else:
	        print("Some error")
	        
	        
#######################End Of Tasktracker Configuration ##################################

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
	        print("Your Jobtracker is successfully configured...")
        else:
	        print("Some error")
	        
	        
#####################  End of JobTracker Configuration ###########################
	        

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
        
        
maxm=maxm+2
minm=minm+2


lines = open('hdfs_unused.txt').readlines()

open('hdfs_unused.txt', 'w').writelines(lines[maxm:])
open('hdfs_used.txt', 'a').writelines(lines[0:maxm])

ipaddr = open('hdfs_used.txt','r').readlines()

name_ip='a'
job_ip='a'
i=0
j=0
k=0
var=0

print minm
print maxm




ip= ipaddr[0].rstrip()

commands.getstatusoutput("sudo sshpass -p 'p' ssh -o stricthostkeychecking=no {0} systemctl start docker".format(ip))
cmd = "sudo sshpass -p 'p' ssh {0} docker run -dit --name name{1} cluster:v4".format(ip,i)
commands.getstatusoutput(cmd)
i=i+1

ip= ipaddr[1].rstrip()
commands.getstatusoutput("sudo sshpass -p 'p' ssh -o stricthostkeychecking=no {0} systemctl start docker".format(ip))
cmd = "sudo sshpass -p 'p' ssh {0} docker run -dit --name job{1} cluster:v5".format(ip,j)
commands.getstatusoutput(cmd)
j=j+1

#minm = minm-2
while k<int(minm-2):
        ip= ipaddr[k+2].rstrip()
        password="p"
        print ip
        #k1=3
        commands.getstatusoutput("sudo sshpass -p 'p' ssh -o stricthostkeychecking=no {0} systemctl start docker".format(ip)) 
        commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} lvcreate --size 2G --name data{2} vgcloud".format(password,ip,k))
        commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkfs.ext4 /dev/vgcloud/data{2}".format(password,ip,k))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p /data{2}".format(password,ip,k))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mount /dev/vgcloud/data{2} /data{2}".format(password,ip,k))

        commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker run -dit -v /data{2}:/data{2} --name data{2} cluster:v4".format(password,ip,k))
             
        commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker run -dit --name task{2} cluster:v6".format(password,ip,k))
                         
                         
        k=k+1 


if maxm==no_task_tracker+2:
        while k<int(maxm-2):
                task_ip= ipaddr[k+2].rstrip()
                password="p"
                containerName="task"+str(k)
                commands.getstatusoutput("sudo sshpass -p {0} ssh {1} systemctl start docker".format(password,task_ip))
                
                commands.getstatusoutput("sudo sshpass -p {0} ssh {1} docker run -dit --name {2} cluster:v6".format(password,task_ip,containerName))
		k=k+1 
		
		
		
if maxm==no_data_node+2:
        while k<int(maxm-2):
                slaveIp= ipaddr[k+2].rstrip()
                password='p'
                containerName="data"+str(k)
                commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} lvcreate --size 2G --name {2} vgcloud".format(password,slaveIp,containerName))

                commands.getstatusoutput("echo 'y' | sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkfs.ext4 /dev/vgcloud/{2}".format(password,slaveIp,containerName))

                commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mkdir -p {2}".format(password,slaveIp,containerName))

                commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} mount /dev/vgcloud/{2} /{2}".format(password,slaveIp,containerName))

                commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} docker run -dit -v /{2}:/{2} --name {2} cluster:v4".format(password,slaveIp,containerName))
      
	        k=k+1 


var=0
i=0
j=0
k=0
    
while var<int(minm):
        if var==0:
        
                ip= ipaddr[var].rstrip()
                print ip
                
                name_ip = commands.getstatusoutput("sudo sshpass -p 'p' ssh {0} docker inspect name{1} | jq '.[].NetworkSettings.Networks.bridge.IPAddress' ".format(ip,i))
                name_ip=name_ip[1].strip('"')
                
                print name_ip
	        configure_namenode(name_ip,ip,"name"+str(i))
		i=i+1
		
		
		
	elif var==1:
                ip= ipaddr[var].rstrip()
                
                job_ip = commands.getstatusoutput("sudo sshpass -p 'p' ssh {0} docker inspect job{1} | jq '.[].NetworkSettings.Networks.bridge.IPAddress' ".format(ip,j))
                job_ip = job_ip[1].strip('"')
                
                configure_jobtracker(name_ip,job_ip,ip,"job"+str(j))
		j=j+1	
		
	
	else:
	        ip= ipaddr[var].rstrip()
	        configure_datanode(ip,name_ip,"data"+str(k))
	        configure_tasktracker(ip,job_ip,"task"+str(k))
		k=k+1 
		      
        var = var+1
        
'''  

if maxm==no_task_tracker+2:
        while var<maxm:
                ip= ipaddr[var].rstrip()
                configure_tasktracker(ip,job_ip,"task"+str(k))
		k=k+1 
		var=var+1
		
elif maxm==no_data_node+2:
        while var<maxm:
                ip= ipaddr[var].rstrip()
                configure_datanode(ip,name_ip,"data"+str(k))
		k=k+1 
		var=var+1




'''
