# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# For example,

# A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5

class Solution:
	# @param A: list of integers
	# @return an integer

	def maxArr(self, A):
		az = []
		au = []

		for i in range(len(A)):

			az.append(A[i]+i)
			au.append(A[i]-1)

		m1, m2 = (min(az), max(az))
		m3, m4 = (min(au), max(au))

		return max(abs(m1-m2), abs(m3-m4))