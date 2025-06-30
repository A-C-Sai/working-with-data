#This program accept list of names dynamically by using list comprehension and sort them
#listsortcompre1.py
def disp(k):
	print("-"*40)
	for val in k:
		print("\t{}".format(val))
	else:
		print("-"*40)

def  sortelements(lst):
	print("Original Elements")
	disp(lst)
	lst.sort()
	print("Sorted Elements in Ascending Order")
	disp(lst)
	lst.reverse() #     or  lst.sort(reverse=True)
	print("Sorted Elements in Decending Order")
	disp(lst)

#main program
print("Enter List of Names separated by comma:") 
lst=  [ str(val)  for val  in input().split(",") ]
sortelements(lst)





