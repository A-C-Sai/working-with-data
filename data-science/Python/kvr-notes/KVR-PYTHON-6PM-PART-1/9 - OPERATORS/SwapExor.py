#Program for swapping two Integer values by using XOR
#SwapExor.py
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
print("-"*50)
print("Original value of a:",a)
print("Original value of b:",b)
print("-"*50)
#Logic for Swapping
a=a^b
b=a^b
a=a^b
print("Swapped value of a:",a)
print("Swapped value of b:",b)
print("-"*50)
