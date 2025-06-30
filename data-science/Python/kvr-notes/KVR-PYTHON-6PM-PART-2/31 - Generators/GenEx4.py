#Program for demonstrating generators--decided toi generate 0 to 5(6-1)
#GenEx4.py
def  kvrrange(start,stop,step):
	while(start<=stop):
		yield start
		start=start+step # OR start+=step

#main program
kr=kvrrange(100,180,10) # 
print(next(kr)) # 100
print(next(kr)) # 110
print(next(kr)) # 120
print("================")
while True:
	try:
		print(next(kr)) # 130----180
	except StopIteration:
		print("================")
		break
