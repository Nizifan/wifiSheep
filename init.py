import os
from analyzer import analyze
import thread
import pexpect


iterator = 1

password = ""

while 1:
	child = pexpect.spawn("ssh root@10.0.0.1 'tcpdump -c 10 -w - -s 0 port not 22' >> ~/code/py/wifi-sheep/data" + str(iteerator) + ".cap"")
	child.expect("root@10.0.0.1's password:")
	child.sendline(password)
	print("get package " + str(iterator) + " from server")
	try:
   		thread.start_new_thread( analyze, str(iterator) )
	except:
   		print("Error: unable to start thread")	
	iterator += 1
