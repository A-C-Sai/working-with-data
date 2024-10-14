#Program for filtering list of vowels from given Line of text
#FilterEx5.py
line=input("Enter Line of Text:")
vwlist=list(filter(lambda ch: ch.lower() in ['a','e','i','o','u'], line))
print("-"*50)
print("Given Line:{}".format(line))
print("Vowels List:{}".format(vwlist))
print("Number of Vowels={}".format(len(vwlist)))
print("-"*50)