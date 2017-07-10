#!/usr/bin/python2


import cgi
import commands

print "content-type:  text/html"
print


fdata=cgi.FormContent()['fname'][0]

fh=open('/webcontent/scripts/uploads/red.py' , 'w')
fh.write(fdata)
fh.close()

fi  = open('oppy.txt')
ip = fi.readlines()
ip=ip[0]
ip=ip.strip()

commands.getstatusoutput('sudo sshpass -p p scp /webcontent/scripts/uploads/red.py {0}:/had_test/'.format(ip))
commands.getstatusoutput("sudo sshpass -p p ssh -o stricthostkeychecking=no {0} docker cp /had_test/red.py client:/".format(ip))

############################# Starting analysis ################################

commands.getstatusoutput('sudo sshpass -p p ssh -o stricthostkeychecking=no {0} hadoop fs -rmr /output'.format(ip))

cmd="sudo sshpass -p p ssh -o stricthostkeychecking=no {0} docker exec client hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar   -input /data.txt   -file map.py -mapper  ./map.py  -file  red.py  -reducer  ./red.py   -output  /output".format(ip)
commands.getstatusoutput(cmd)

status=commands.getstatusoutput("sudo sshpass -p p ssh -o stricthostkeychecking=no {0} docker exec client hadoop fs -cat /output/part-00000".format(ip))

status = status[1]
print status



