import math
import random

def Gen_Beam(radius):
	coord = []
	for i in list(range(50)):
		theta = 2*math.pi*random.uniform(0,1)
		r = radius*math.sqrt(random.uniform(0,1))
		x = r*math.cos(theta)
		y = r*math.sin(theta)
		coord.append([[x],[y]])
	return coord
