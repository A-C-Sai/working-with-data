#Program for demonstrating break statement
#breakex2.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-"*50)
print("------------------------------")
print("By using while loop with break")
i=0
while(i<len(s)):
    if(s[i]=="H"):
        break
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("i am from while-else loop")
print("i am from other statementrs in program")


