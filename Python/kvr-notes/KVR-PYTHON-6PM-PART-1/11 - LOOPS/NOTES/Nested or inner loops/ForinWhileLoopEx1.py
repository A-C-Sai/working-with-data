#Program for demonstarting Inner Loops-----for loop in while  loop
#ForinWhileLoopEx1.py
i=1
while(i<=5):
	print("Outer while Loop--Value of i={}".format(i))
	print("-"*50)
	for j in range(3,0,-1):
		print("\tInner  For Loop--Value of j={}".format(j))
	else:
		i=i+1
		print("\tPVM Comes out of inner for loop")
		print("-"*50)
else:
	print("\tPVM Comes out of Outer while loop")

"""
E:\KVR-PYTHON-6PM\LOOPS>py ForinWhileLoopEx1.py
Outer while Loop--Value of i=1
--------------------------------------------------
        Inner  For Loop--Value of j=3
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=1
        PVM Comes out of inner for loop
--------------------------------------------------
Outer while Loop--Value of i=2
--------------------------------------------------
        Inner  For Loop--Value of j=3
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=1
        PVM Comes out of inner for loop
--------------------------------------------------
Outer while Loop--Value of i=3
--------------------------------------------------
        Inner  For Loop--Value of j=3
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=1
        PVM Comes out of inner for loop
--------------------------------------------------
Outer while Loop--Value of i=4
--------------------------------------------------
        Inner  For Loop--Value of j=3
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=1
        PVM Comes out of inner for loop
--------------------------------------------------
Outer while Loop--Value of i=5
--------------------------------------------------
        Inner  For Loop--Value of j=3
        Inner  For Loop--Value of j=2
        Inner  For Loop--Value of j=1
        PVM Comes out of inner for loop
--------------------------------------------------
        PVM Comes out of Outer while loop
"""