#Program for Demonstrating Possitioan arguments
#PossArgsEx1.py
def  dispstudinfo(sno,sname,marks ):
	print("\t{}\t{}\t{}".format(sno,sname,marks))

#main program
print("-"*50)
print("\tSno\tName\t\tMarks")
print("-"*50)
dispstudinfo(10,"Samir  ",23.45) # Function Call
dispstudinfo(20,"Zohar   ",33.45) # Function Call
dispstudinfo(30,"Dilip   ",43.45) # Function Call
dispstudinfo(40,"Aditya   ",53.45) # Function Call
print("-"*50)