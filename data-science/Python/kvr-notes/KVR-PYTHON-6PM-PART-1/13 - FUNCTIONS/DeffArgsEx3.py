#Program for Demonstrating Default arguments
#DeffArgsEx3.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="India" ):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("-"*50)
print("\tSno\tName\t\tMarks\tCourse\tCountry")
print("-"*50)
dispstudinfo(10,"Samir    ",23.45) # Function Call
dispstudinfo(20,"Zohar      ",33.45) # Function Call
dispstudinfo(30,"Dilip      ",43.45) # Function Call
dispstudinfo(40,"Aditya   ",53.45) # Function Call
dispstudinfo(50,"Donald   ",13.45) # Function Call

print("-"*50)
