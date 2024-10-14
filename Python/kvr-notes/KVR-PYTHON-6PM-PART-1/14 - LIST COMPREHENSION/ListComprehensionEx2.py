#ListComprehensionEx2.py
lst=[2,6,3,9,12,16,25]
sqlist=[ val**2  for val in lst   ]
for on,sn in zip(lst,sqlist):
	print("\t{}--->{}".format(on,sn))
