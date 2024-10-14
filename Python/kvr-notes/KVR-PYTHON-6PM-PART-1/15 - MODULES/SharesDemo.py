#SharesDemo.py---main program--Viewing
import Shares,time,importlib  # Now a days--imp module deprecated in favour of importlib
def dispshares(dictobj):
	print("-"*50)
	print("\tShares Name\tShare Value:")
	print("-"*50)
	for sn,sv in dictobj.items():
		print("\t{}\t\t{}".format(sn,sv))
	print("-"*50)


#main program
dictobj=Shares.shareinfo() # Function Call
dispshares(dictobj)
print("at Line-15--Going to sleep for 15 secs")
time.sleep(15)
print("at Line-17--Coming out-of sleep ")
importlib.reload(Shares)
dictobj=Shares.shareinfo() # Function Call
dispshares(dictobj)
print("at Line-21--Going to sleep for 15 secs")
time.sleep(15)
print("at Line-23--Coming out-of sleep ")
importlib.reload(Shares)
dictobj=Shares.shareinfo() # Function Call
dispshares(dictobj)