#Program for demonstrating Keyword Arguments
#kwdargsEx2.py
def  dispstudInfo(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("-"*50)
print("\tSno\tName\tMarks\tCourse")
print("-"*50)
dispstudInfo(10,"RS",11.22)
dispstudInfo(marks=22.22,sno=20,sname="TR")
dispstudInfo(30,marks=44.44,sname="MC")
dispstudInfo(crs="Java",sno=40,marks=11.11,sname="Trump")
dispstudInfo(10,"Joe ",marks=33.33)
dispstudInfo(crs="War",sname="Putin",marks=22.22,sno=50)
print("-"*50)