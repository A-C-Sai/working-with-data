#Porogram for fcopying the content of one file into another file
#ImageFileCopy.py
def  copyprocess():
	sfile=input("Enter Image Source File:")
	try:
		with open(sfile,"rb") as rp:
			dfile=input("Enter Image Destination File:")
			with open(dfile,"ab") as wp:
				#read the image data from Source Image File
				srcfiledata=rp.read()
				#write Source Image data into Destination Image file
				wp.write(srcfiledata)
				print("\n1 file(s) copied")
	except FileNotFoundError:
		print("Source File does not exist")

#main program
copyprocess()