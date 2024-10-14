#Create a new file stud2.data by using "with open() as "
#FileOpenEx3.py
with open("stud2.data","w") as fp:
	print("-"*50)
	print("type of fp=",type(fp))
	print("File Opened in write mode successfully")
	print("Name of the file=",fp.name)
	print("File Mode=",fp.mode)
	print("Is this file readable?=",fp.readable())
	print("Is this file writable?=",fp.writable())
	print("is this file closed within in Indentation block with open()=",fp.closed) # False
	print("-"*50)

print("is this file closed Out-of Indentation block- with open()=",fp.closed) # True
