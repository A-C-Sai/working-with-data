#runclock.py
while(True):
	from datetime import datetime
	now=datetime.now()
	sc="%s:%s:%s" %(now.hour,now.minute,now.second)
	print("\t\t\t",sc,end="\r")