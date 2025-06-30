#ListComprehensionEx3.py
print("Enter List of Values separated by space")
lst=[ int(val) for val in input().split()]
print("Given List:{}".format(lst))
print("-"*60)
print("\nEnter List of Names separated by Comma")
nameslist=[name for name in input().split(",")]
print("Given Names:{}".format(nameslist))
