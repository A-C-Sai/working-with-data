#Porogram for fcopying the content of one file into another file
#FileCopy.py
def  copyprocess():
	sfile=input("Enter Source File:")
	try:
		with open(sfile,"r") as rp:
			dfile=input("Enter Destination File:")
			with open(dfile,"a") as wp:
				#read the data from Source File
				srcfiledata=rp.read()
				wp.write(srcfiledata)
				print("\n1 file(s) copied")
	except FileNotFoundError:
		print("Source File does not exist")

#main program
copyprocess()