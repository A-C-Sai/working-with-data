#Open the file stud.data in read mode
#FileOpenEx1.py
try:
    fp=open("stud.data","r")
except FileNotFoundError:
    print("File does not exist")
else:
    print("-" * 50)
    print("File Opened in read Mode Sucessfully")
    print("type of fp=", type(fp))
    print("Name of the file=", fp.name)
    print("File Mode=", fp.mode)
    print("Is this file readable?=", fp.readable())
    print("Is this file writable?=", fp.writable())
    print("is this file closed before close()?=", fp.closed)  # False
finally:
    print("i am from finally block")
    fp.close()
    print("is this file closed after close()?=", fp.closed)  # False
