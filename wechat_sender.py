# -*-coding:utf-8 -*-
import sys  
#reload(sys)
#sys.setdefaultencoding('utf8')
import itchat
from itchat.content import TEXT
from itchat.content import *
import time
import os
def send_to_all_teacher():
	friends=itchat.get_friends(update=True)[0:]
	teachers=[]
	for friend in friends:
		#print(friend)
		if '老师' in friend['RemarkName']:#检验备注中是否有老师两个字段
			#teachers.append(friend)
			send_message="%s老师：祝福语，敬上。"%friend['RemarkName'][0:1]
			print("已发送给:",friend['RemarkName'],send_message)
			itchat.send(send_message,friend['UserName'])
			time.sleep(1)
	#init_UI_teacher(teachers)
	#print "Send OK!"
if __name__=='__main__':
	itchat.auto_login()
	send_to_all_teacher()

  