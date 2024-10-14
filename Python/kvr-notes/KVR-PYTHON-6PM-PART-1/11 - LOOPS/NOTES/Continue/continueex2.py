#Program for demostrating continue stmt
#continueex2.py
s="PYTHON"
for ch in s:
    if(ch=="Y") or (ch=="H"):
        continue
    print("\t{}".format(ch),end=" ") # PTON
else:
    print("\ni am from for-else loop")