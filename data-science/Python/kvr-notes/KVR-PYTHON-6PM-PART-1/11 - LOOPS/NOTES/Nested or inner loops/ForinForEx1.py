#Program for demonstarting Inner Loops-----for loop in for loop
#ForinForEx1.py
for i in range(1,6):
	print("Outer For Loop--Value of i={}".format(i))
	print("-"*50)
	for j in range(1,4):
		print("\tInner  For Loop--Value of j={}".format(j))
	else:
		print("\tPVM Comes out of inner for loop")
		print("-"*50)
else:
	print("\tPVM Comes out of Outer for loop")

"""
E:\KVR-PYTHON-6PM\LOOPS>py ForinForEx1.py
Outer For Loop--Value of i=1
--------------------------------------------------
        Inner  For Loop--Value of j=1
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=3
        PVM Comes out of inner for loop
--------------------------------------------------
Outer For Loop--Value of i=2
--------------------------------------------------
        Inner  For Loop--Value of j=1
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=3
        PVM Comes out of inner for loop
--------------------------------------------------
Outer For Loop--Value of i=3
--------------------------------------------------
        Inner  For Loop--Value of j=1
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=3
        PVM Comes out of inner for loop
--------------------------------------------------
Outer For Loop--Value of i=4
--------------------------------------------------
        Inner  For Loop--Value of j=1
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=3
        PVM Comes out of inner for loop
--------------------------------------------------
Outer For Loop--Value of i=5
--------------------------------------------------
        Inner  For Loop--Value of j=1
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=3
        PVM Comes out of inner for loop
--------------------------------------------------
        PVM Comes out of Outer for loop

"""










