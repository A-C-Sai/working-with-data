def flatten(lst,container):
	print(id(container))
	for element in lst:
		if hasattr(element,'__iter__'):
			flatten(element,container)
		else:
			container.append(element)
			


if __name__ == '__main__':
	
	lst = [[[[[[[8]]]]]]]
	container = []
	flatten(lst,container)
	print(container)




