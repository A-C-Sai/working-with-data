#Program for demostrating continue stmt
#continueex1.py
s="PYTHON"
for ch in s:
    if(ch=="H"):
        continue
    else:
        print("\t{}".format(ch),end=" ")
else:
    print("\ni am from for-else loop")