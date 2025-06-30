import pickle


d1= 15
d2= 15.0
d3= True
d4= 2+3j
d5= 'str'
d6= bytes([1,2,3])
d7= bytearray([1,2,3,4])
d8= range(10)
d9= [1,2,3,4,5]
d10= (1,2)
d11= {1,2,3}
d12= frozenset({4,5,6,7})
d13= {"a":'apple',"b":'ball'}
d14= None

try:
	with open('dataPick.txt','wb') as fp:
		pickle.dump(d1,fp)
		pickle.dump(d2,fp)
		pickle.dump(d3,fp)
		pickle.dump(d4,fp)
		pickle.dump(d5,fp)
		pickle.dump(d6,fp)
		pickle.dump(d7,fp)
		pickle.dump(d8,fp)
		pickle.dump(d9,fp)
		pickle.dump(d10,fp)
		pickle.dump(d11,fp)
		pickle.dump(d12,fp)
		pickle.dump(d13,fp)
		pickle.dump(d14,fp)

except FileNotFoundError:
	print('This file not found')
