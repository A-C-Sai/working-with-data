'''
nCr = n!/((n-r)!*r!)

n :- row number starts from 0
r :- [0,n]

initial row : 1
next row : 
	initial row + 0
		   +
	0 + inital row shifted to right
'''

def pascal(rows,/):
	row = [1]
	for i in range(rows):
		print(row)
		row,temp = row[:]+[0],[0]+row[:]
		row = [ x+y for x,y in zip(row,temp)]

if __name__ == '__main__':
	pascal(10)