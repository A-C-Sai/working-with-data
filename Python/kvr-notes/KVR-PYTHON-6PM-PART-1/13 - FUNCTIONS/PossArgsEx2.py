#Program for Demonstrating Possitioan arguments
#PossArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs ):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("-"*50)
print("\tSno\tName\t\tMarks\tCourse")
print("-"*50)
dispstudinfo(10,"Samir    ",23.45,"Python") # Function Call
dispstudinfo(20,"Zohar   ",33.45,"Python") # Function Call
dispstudinfo(30,"Dilip   ",43.45,"Python") # Function Call
dispstudinfo(40,"Aditya   ",53.45,"Python") # Function Call
print("-"*50)