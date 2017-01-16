import os
from analyzer import analyze

while 1:
	os.system("~/Downloads/sshpass-1.05/sshpass -p intuo@123 ssh root@10.0.0.1 'tcpdump -c 1000 -w - port not 22' >> ~/code/py/wifi-sheep/data.cap")
	analyze()
	os.system("rm data.cap")
