# Python 3

class Solution:
	# @param A: integer
	# @param B: integer
	# @param C: integer
	# @param D: integer
	# @return an integer
	def solve(self, A, B, C, D):
		if (A == B and C == D):
			return 1
		if (A == C and B == D):
		    return 1 
		if (A == D and B == C):
			return 1
		else:
			return 0