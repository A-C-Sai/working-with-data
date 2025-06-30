#StudentEx1.py
class Student:pass
#main program
s1=Student() # Object Creation
s2=Student() # Object Creation
print("Content of s1 before adding data=", s1.__dict__) # {}
s1.sno=10
s1.sname="RS"
s1.marks=34.56 # here we specified Instance Data memebrs b y using Object name
print("Content of s1 after adding data=", s1.__dict__) # {sno:10,sname:RS,marks:34.56}
print("-"*50)
print("Content of s2 before adding data=", s2.__dict__) # {}
s2.stno=20
s2.name="TR"
s2.marks=44.44
s2.dob="26-01-2023" # here we specified Instance Data memebrs b y using Object name
print("Content of s2 after adding data=", s2.__dict__) # 
