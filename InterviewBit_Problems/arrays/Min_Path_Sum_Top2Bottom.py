
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# class Solution(object):
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minimumTotal(self, A,):
		''' type A = List[List[int]]
		return type: int
		'''

		M, N = len(A), len(A[0])
		cost = [float('int')] * N

		for i in range(M):
			cost[0] = A[i][0] + cost[0] if i > 0 else A[i][0]
			for j in range(1, N):
				cost[j] = min(cost[j-1], cost[j]) + A[i][j]

		return cost[-1]


# O(n) runtime solution here