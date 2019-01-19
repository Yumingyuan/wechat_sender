# -*-coding:utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   
import itchat
from itchat.content import TEXT
from itchat.content import *
import time
import os
def send_to_all_teacher():
	friends=itchat.get_friends(update=True)[0:]
	teachers=[]
	for friend in friends:
		if '老师' in friend['RemarkName']:#检验备注中是否有老师两个字段
			send_message="%s老师：祝福语，敬上。"%friend['RemarkName'][0:1]
			print u"已发送给:",friend['RemarkName'],send_message
			itchat.send(send_message,teacher['UserName'])
			time.sleep(1)
	print "Send OK!"
if __name__=='__main__':
  itchat.auto_login()
  send_to_all_teacher()

  