#Program for demonstrating break statement
#breakex3.py
lst=["Python","Data Science","Django","Java","Adv Java"]
for crs in lst:
    if(crs==lst[2]):
        break
    print("\t{}".format(crs))
