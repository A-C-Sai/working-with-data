#Program swapping of two values by using multi line assigment
#SwapEx.py
a=input("Enter Value of a:")
b=input("Enter Value of b:")
print("-"*40)
print("Original Val of a={}".format(a))
print("Original Val of b={}".format(b))
print("-"*40)
#Swapping logic
a,b=b,a  # multi line assigment
print("Swapped Val of a={}".format(a))
print("Swapped Val of b={}".format(b))
print("-"*40)
