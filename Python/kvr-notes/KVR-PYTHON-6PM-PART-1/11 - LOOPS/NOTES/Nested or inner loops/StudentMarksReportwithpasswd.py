#Program for student marks report
#StudentMarksReportwithpasswd.py
#accept Student Number
import getpass
while(True):
	pwds=getpass.getpass(prompt="Enter ur password:")
	if(pwds=="KVR"):
		break
	print("Invalid Password, try again")

while(True):
	sno=int(input("Enter Student Number(100-200):"))
	if(200>=sno>=100):
		break
	print("Invalid Student Number-Try again")

#Accept Student Name
sname=input("Enter Student Name:")
#accept C lang Marks--100
while(True):
	cm=int(input("Enter Marks C:")) # 99
	if(0<=cm<=100):
		break
	print("Invalid Marks in C--try again")
#accept C++ lang Marks--100
while(True):
	cpp=int(input("Enter Marks C++:")) # 56
	if(0<=cpp<=100):
		break
	print("Invalid Marks in C++--try again")
#accept Python lang Marks--100
while(True):
	pym=int(input("Enter Marks Python:")) 
	if(0<=pym<=100):
		break
	print("Invalid Marks in Python--try again")
#cal total marks and percentage of marks
totmarks=cm+cpp+pym
percent=(totmarks/300)*100
#Decide the grade for fail or pass
if(cm<40) or   (cpp<40)  or   (pym<40) :
	grade="FAIL"
else:
	#deciding Passed Grade
	if(totmarks>=250)  and   (totmarks<=300):
		grade="DISTINCTION"
	elif(totmarks>=200)  and   (totmarks<=249):
		grade="FIRST"
	elif(totmarks>=150)  and   (totmarks<=199):
		grade="SECOND"
	elif(totmarks>=120)  and   (totmarks<=149):
		grade="THIRD"

#Dislay Marks Report	
print("="*50)
print("\tS t u d e n t  M a r k s  R e p o r t")
print("="*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in C++:{}".format(cpp))
print("\tStudent Marks in Python:{}".format(pym))
print("-"*50)
print("\tStudent Total Marks :{}".format(totmarks))
print("\tStudent Percent of Marks :{}".format(round(percent,2)))
print("\tStudent Exam Result :{}".format(grade))
print("-"*50)
print("="*50)





