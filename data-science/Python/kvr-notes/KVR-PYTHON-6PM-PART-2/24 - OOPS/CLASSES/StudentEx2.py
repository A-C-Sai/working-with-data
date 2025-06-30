#StudentEx2.py
class Student:pass
#main program
s1=Student() # Object Creation
s2=Student() # Object Creation
#Specify the Instance Data members of s1 by using object name
s1.sno=10
s1.name="RS"
s1.marks=33.33
#Specify the Instance Data members of s2 by using object name
s2.stno=20
s2.name="TR"
s2.marks=44.44
#Display the data of s1 object
print("Content of s1 object")
print(s1.sno,s1.name,s1.marks)
print("Content of s2 object")
print(s2.stno,s2.name,s2.marks)
print("---------------------OR--------------------------------")
print("Content of s1 object")
for k,v in s1.__dict__.items():
	print("\t{}-->{}".format(k,v))
print("Content of s2 object:")
for k,v in s2.__dict__.items():
		print("\t{}==>{}".format(k,v))
print("---------------------OR--------------------------------")
print("Content of s1 object")
print("Student Number:{}".format(s1.sno))
print("Student Name:{}".format(s1.name))
print("Student Marks:{}".format(s1.marks))
print("Content of s2 object")
print("Student Number:{}".format(s2.stno))
print("Student Name:{}".format(s2.name))
print("Student Marks:{}".format(s2.marks))


