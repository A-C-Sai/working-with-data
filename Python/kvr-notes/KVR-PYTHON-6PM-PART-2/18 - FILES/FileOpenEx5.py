#Create a new file stud2.data by using "with open() as "
#FileOpenEx5.py
try:
	with open("kvr1.data","x+") as fp:
		print("-"*50)
		print("type of fp=",type(fp))
		print("File Opened in EXclusive  mode successfully")
		print("Name of the file=",fp.name)
		print("File Mode=",fp.mode)
		print("Is this file readable?=",fp.readable())
		print("Is this file writable?=",fp.writable())
		print("is this file closed within in Indentation block with open()=",fp.closed) # False
		print("-"*50)
	print("is this file closed Out-of Indentation block- with open()=",fp.closed) # True
except FileExistsError:
	print("File already exist")
