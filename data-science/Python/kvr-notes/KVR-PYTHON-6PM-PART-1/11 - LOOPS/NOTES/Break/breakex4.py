#Program for demonstrating break statement
#breakex4.py
r=range(10,110,10)
for val in r:
    if(val==70):
        break
    else:
        print("\t{}".format(val))