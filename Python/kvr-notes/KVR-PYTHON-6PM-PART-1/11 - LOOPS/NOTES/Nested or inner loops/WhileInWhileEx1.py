#Program for demonstarting Inner Loops-----while loop in while loop
#WhileInWhileEx1.py
i=1
while(i<=5):
	print("Outer while Loop--Value of i={}".format(i))
	print("-"*50)
	j=1
	while(j<=3):
		print("\tInner  while Loop--Value of j={}".format(j))
		j=j+1
	else:
		i=i+1
		print("\tPVM Comes out of inner while loop")
		print("-"*50)
else:
	print("\tPVM Comes out of Outer whileloop")

"""
E:\KVR-PYTHON-6PM\LOOPS>py WhileInWhileEx1.py
Outer while Loop--Value of i=1
--------------------------------------------------
        Inner  while Loop--Value of j=1
        Inner  while Loop--Value of j=2
        Inner  while Loop--Value of j=3
        PVM Comes out of inner while loop
--------------------------------------------------
Outer while Loop--Value of i=2
--------------------------------------------------
        Inner  while Loop--Value of j=1
        Inner  while Loop--Value of j=2
        Inner  while Loop--Value of j=3
        PVM Comes out of inner while loop
--------------------------------------------------
Outer while Loop--Value of i=3
--------------------------------------------------
        Inner  while Loop--Value of j=1
        Inner  while Loop--Value of j=2
        Inner  while Loop--Value of j=3
        PVM Comes out of inner while loop
--------------------------------------------------
Outer while Loop--Value of i=4
--------------------------------------------------
        Inner  while Loop--Value of j=1
        Inner  while Loop--Value of j=2
        Inner  while Loop--Value of j=3
        PVM Comes out of inner while loop
--------------------------------------------------
Outer while Loop--Value of i=5
--------------------------------------------------
        Inner  while Loop--Value of j=1
        Inner  while Loop--Value of j=2
        Inner  while Loop--Value of j=3
        PVM Comes out of inner while loop
--------------------------------------------------
        PVM Comes out of Outer whileloop