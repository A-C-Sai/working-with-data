#Program for Demonstrating Default arguments
#DeffArgsEx2.py
def  dispstudinfo1(sno,sname,marks,crs="PYTHON" ):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

def  dispstudinfo2(sno,sname,marks,crs="Java" ):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("-"*50)
print("\tSno\tName\t\tMarks\tCourse")
print("-"*50)
dispstudinfo1(10,"Samir    ",23.45) # Function Call
dispstudinfo1(20,"Zohar   ",33.45) # Function Call
dispstudinfo1(40,"Aditya   ",53.45) # Function Call
dispstudinfo1(60,"Biden   ",83.45) # Function Call
print("-"*50)
print("\tSno\tName\t\tMarks\tCourse")
print("-"*50)
dispstudinfo2(30,"Dilip   ",43.45) # Function Call
dispstudinfo2(50,"Trump   ",53.45) # Function Call
dispstudinfo2(70,"Shoeb   ",63.45) # Function Call
print("-"*50)