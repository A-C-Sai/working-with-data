def flatten(lst,/):
	
	for element in lst:
		if hasattr(element,'__iter__'):
			yield from flatten(element)
		else:
			yield element

			





if __name__ == '__main__':
	
	
	lst_flatten = flatten([1,2,[3,4,[5,6],7],8])	
	for i in range(8):
		print(next(lst_flatten))