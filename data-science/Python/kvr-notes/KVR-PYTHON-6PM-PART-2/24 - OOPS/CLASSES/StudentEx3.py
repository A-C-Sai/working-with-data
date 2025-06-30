#StudentEx3.py
class Student:
	crs="PYTHON" # Class Level Data Members--Inside Class Def 
	
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
print(s1.sno,s1.name,s1.marks,Student.crs)
print("Content of s2 object")
print(s2.stno,s2.name,s2.marks,Student.crs)

