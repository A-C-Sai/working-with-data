#Program for demonstrating generators--decided toi generate 0 to 5(6-1)
#GenEx3.py
def  kvrrange(start,stop):
	while(start<=stop):
		yield start
		start=start+1 # OR start+=1

#main program
kr=kvrrange(10,20) # 
print(next(kr)) # 10
print(next(kr)) # 11
print("================")
while True:
	try:
		print(next(kr)) # 12--20
	except StopIteration:
		print("================")
		break
