# -*-coding:utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   
import itchat
from itchat.content import TEXT
from itchat.content import *
import time
import os
from Tkinter import *
root=Tk()
listb_teacher=Listbox(root,selectmode=EXTENDED)
scroll_bar_teacher=Scrollbar(root)
#side指定Scrollbar为居右；fill指定填充满整个剩余区域。
scroll_bar_teacher.pack(side=RIGHT,fill=Y)
#下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set
listb_teacher['yscrollcommand'] = scroll_bar_teacher.set
var=IntVar()
Ra_Button1=Radiobutton(root, text="全选", variable=var, value=1)
Ra_Button1.pack( anchor = W )
Ra_Button2=Radiobutton(root, text="反选", variable=var, value=2)
Ra_Button2.pack( anchor = W )
def init_UI_teacher(list):
	for item in list:
		listb_teacher.insert(0,item['RemarkName'])
	listb_teacher.pack()
	root.mainloop()
def send_to_all_teacher():
	friends=itchat.get_friends(update=True)[0:]
	teachers=[]
	for friend in friends:
		if '老师' in friend['RemarkName']:#检验备注中是否有老师两个字段
			teachers.append(friend)
			#send_message="%s老师：祝福语，敬上。"%friend['RemarkName'][0:1]
			#print u"已发送给:",friend['RemarkName'],send_message
			#itchat.send(send_message,teacher['UserName'])
			#time.sleep(1)
	init_UI_teacher(teachers)
	#print "Send OK!"
if __name__=='__main__':
  itchat.auto_login()
  send_to_all_teacher()

  