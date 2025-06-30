#continueex3.py
#Display +Ve Values
lst=[10,-34,-56,23,-56,78,123]
for val in lst:
    if(val>0):
        continue
    print("\t{}".format(val))