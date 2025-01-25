import pickle 

try:
	with open('dataPick.txt','rb') as fp:
	

		while(True):
			data = pickle.load(fp)
			print(data)


except FileNotFoundError:
	print('This file not found')
except EOFError:
	print('Reached End Of File')
