#Program for demonstrating break statement
#breakex1.py
s="PYTHON"
print("By using For loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("-"*50)
print("\nfor loop with break statement")
for ch in s:
    if(ch=="H"):
        break
    else:
        print("\t{}".format(ch))
else:
    print("i am from for--else loop")
print("Other statements in Program")
