#Program for random accessing the data from file--tell() and seek()
#RandomAccessFile.py
try:
	with open("addr1.data","r") as fp:
		print("Initial Pos of fp=",fp.tell())#0
		filedata=fp.read(5)
		print("File Data=",filedata) #
		print("Now Pos of fp=",fp.tell())#5
		print("-------------------------------")
		filedata=fp.read(11)
		print("File Data=",filedata) #
		print("Now Pos of fp=",fp.tell())#
		print("-------------------------------")
		filedata=fp.read()
		print("File Data=",filedata) #
		print("Now Pos of fp=",fp.tell())#
		print("-------------------------------")
		fp.seek(0)
		print("Now Pos of fp=",fp.tell())#0
		filedata=fp.read()
		print("File Data=",filedata) #
		print("Now Pos of fp=",fp.tell())#0
except FileNotFoundError:
		print("Source File does not exist")

