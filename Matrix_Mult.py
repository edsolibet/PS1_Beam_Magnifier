from __future__ import division

def multiple_matrix_mult(*arg):
	temp = list(arg)
	for i in list(range(len(arg)-1)):
		temp[0:2] = [matrix_mult(temp[0], temp[1])]
	return temp[0]

def matrix_mult(a, b):
	res = [[0 for col in list(range(len(b[0])))] for row in list(range(len(a)))]
	for row in list(range(len(b[0]))):
		for colb in list(range(len(b[0]))):
			tot = 0
			for cola in list(range(len(a[0]))):
				tot += a[row][cola] * b[cola][colb]
			res[row][colb] = tot
	return res
