#Program for finding sum of different subjects marks secured by Different students who are studying in different classes
#PureKwdVarLenArgsEx3.py

def  findtotalmarks(sno,sname,cls,cnt="India",**subsmarks):  
	print("="*50)
	print("\tMarks Memo:")
	print("-"*50)
	totmarks=0
	print("\tStudent Number:{}\n\tStudent Name:{}".format(sno,sname))
	print("\tCountry:{}".format(cnt))
	print("-"*50)
	for subject,marks in subsmarks.items():
		print("\t{}\t{}".format(subject,marks))
		totmarks=totmarks+marks
	print("-"*50)
	print("Total Marks:{}".format(totmarks))

#main program
findtotalmarks(111,"Zohir","X",Tel=50,Hindi=80,Eng=88,Maths=99,Sci=88,Soc=66)
findtotalmarks(222,"Rossum","XII",Maths=75,Phy=58,Che=57)
findtotalmarks(333,"Barath","B.Tech",C=50,Cpp=67,OS=77,DBMS=77,SE=66)
findtotalmarks(444,"Vinay","Research")
findtotalmarks(555,"Trump","Politics",cnt="USA",poli=30,eco=45)
findtotalmarks(666,"Joe","Politics",poli=70,eco=85,Civics=66,cnt="USA")