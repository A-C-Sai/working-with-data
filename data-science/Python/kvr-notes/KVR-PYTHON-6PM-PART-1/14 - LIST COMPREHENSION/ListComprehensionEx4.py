#ListComprehensionEx4.py
print("Enter List of Values which Posstive separated by space")
lst=[ int(val) for val in input().split()  if int(val)>0  ]
print("Given Posstive List:{}".format(lst))
print("-"*60)
print("\nEnter List of Names whose length in between 3 and 5 separated by Comma")
nameslist=[name for name in input().split(",") if 3<=len(name)<=5   ]
print("Given Names whise length in between 3 and 5 :{}".format(nameslist))
