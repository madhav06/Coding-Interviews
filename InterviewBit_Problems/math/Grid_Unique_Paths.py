# Python 3 code
'''
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)

'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
		numPaths = [[1 for j in xrange(B)] for i in xrange(A)]
		for i in xrange(1,A):
			for j in xrange(1,B):
				numPaths[i][j] = numPaths[i-1][j] + numPaths[i][j-1]
		return numPaths[-1][-1]

        