#!/usr/bin/env python
#import argparse
from __future__ import division
import sys
import Matrix_Mult
import Generate_Beam

param = (sys.argv)[1:]
param = [int(i) for i in param]
thin_lens_sep = param[1] + param[2]
beam = Generate_Beam.Gen_Beam(param[0])
output = []

#print ("BEAM", beam)
print ("Param: ", param)

def free_space(d):
	return [[1, d], [0, 1]]

def thin_lens(f):
	return [[1, 0], [-1/f, 1]]

fs = free_space(thin_lens_sep)
tl1 = thin_lens(param[1])
tl2 = thin_lens(param[2])
res = Matrix_Mult.multiple_matrix_mult(tl2, fs, tl1)
#	print (free_space(thin_lens_sep))
#	print (thin_lens(param[1]))
#	print (thin_lens(param[2]))
#	print (res)
for pt in beam:
	print ("Point in beam: ", pt)
	temp = Matrix_Mult.multiple_matrix_mult(res, pt)
	print ("Output beam point:", temp)
	output.append(temp)
#print ("OUTPUT", output)
#print (res)
