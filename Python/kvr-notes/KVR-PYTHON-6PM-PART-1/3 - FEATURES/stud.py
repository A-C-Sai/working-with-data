class Student:pass


s=Student()
print("content of s=",s.__dict__)
s.sno=10
s.sname="KVR"
s.marks=22.22
print("content of s=",s.__dict__)
s.cname="OUCET"
print("content of s=",s.__dict__)
s.place="HYD"
print("content of s=",s.__dict__)

