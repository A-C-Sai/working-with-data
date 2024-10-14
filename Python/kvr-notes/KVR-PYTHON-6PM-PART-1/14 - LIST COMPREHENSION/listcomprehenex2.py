#listcomprehenex2.py
print("Enter List of values separated by space:") 
lst=[ int (val)  for val in input().split() ]  # 10 20 34 -45 -56 23
print("\nGiven List of elements:{}".format(lst))
print("================OR=====================")
print("Enter List of values separated by comma:") 
lst=[ int (val)  for val in input().split(",") ]  
print("\nGiven List of elements:{}".format(lst))
