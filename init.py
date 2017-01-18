import os
from MyPassword import password
from analyzer import analyze
import _thread
import pexpect
import sys

iterator = 1

while 1:
	shellCmd = 'ssh root@10.0.0.1 "tcpdump -c 50 -w - -s 0 port not 22" > data' + str(iterator) + '.cap'
	child = pexpect.spawn('/bin/bash',['-c',shellCmd])
	sshNewkey = 'Are you sure you want to continue connecting'
	i = child.expect([pexpect.TIMEOUT, sshNewkey, 'password: '])
	if i == 0:
		print("ERROR:")
		print('SSH could not login. Here is what SSH said:')
		print(child.before, child.after)
		sys.exit()
	if i == 1 :
		child.sendline('yes')
		child.expect('password:')
	child.sendline(password)
	print("dumping in Wi-Fi,please wait")
	child.expect(pexpect.EOF)

	print("get data package" + str(iterator))
	_thread.start_new_thread( analyze, (str(iterator),))
	iterator += 1
