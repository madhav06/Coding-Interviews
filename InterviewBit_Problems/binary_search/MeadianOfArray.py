# Python3

# There are two sorted arrays A and B of size m and n respectively.

# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

# The overall run time complexity should be O(log (m+n)).

# Sample Input

# A : [1 4 5]
# B : [2 3]

# Sample Output

# 3

class Solution:
	# @param A: tuple of integers
	# @param B: tuple of integers
	# @return a double

	def findMedianSortedArrays(self, A, B):

		m,n = len(A), len(B)

		if m > n:
			A, B, m, n = B, A, n, m

		imin, imax, half_len = 0, m, (m+n+1) / 2

		while imin <= imax:

			i = (imin + imax) / 2

			j = half_len - i

			if i < m and B[j-1] > A[i]:

				imin = i + 1

			elif i > 0 and A[i-1] > B[j]:
				imax = i - 1

			else:
				if i == 0: max_of_left = B[j-1]
			    elif j == 0: max_of_left = A[i-1]
			    else: max_of_left = max(A[i-1], B[j-1])

			    if (m + n) % 2 == 1:
			    	return max_of_left

			    if i == m: min_of_right = B[j]
			    elif j == n: min_of_right = A[i]
			    else: min_of_right = min(A[i], B[j])

			    return (max_of_left + min_of_right) / 2.0



	"""
	A = list(A)
	A.extend(B)
	A = sorted(A)
	l = len(A

	if l%2 == 0:
		return (A[int(l/2)-1] + A[int(l/2)])/2.0
	else:
		return A[int(l/2)]



	"""


