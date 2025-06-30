#Program for  reading student records which are present student file by using Un-Pickling
#StudUnPick.py---Program-(B)
import pickle
def   readstudrecords():
	with open("studinfo.data","rb") as fp:
		print("-"*50)
		print("STNO\tNAME\tMARKS")
		print("-"*50)
		while(True):
			try:
				studrec=pickle.load(fp)
				for val in studrec:
					print("{}".format(val),end="\t")
				print()
			except EOFError:
				print("-"*50)
				break
		
#main program
readstudrecords()