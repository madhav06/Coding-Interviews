# Python3

# try this at home again.

# Given a sorted array of integers A(0 based index) of size N, 
# find the starting and ending position of a given integar B in array A.

# Your algorithm’s runtime complexity must be in the order of O(log n).

# Return an array of size 2, 
# such that first element = starting position of B in A and second element = ending position of B in A, 
# if B is not found in A return [-1, -1].

class Solution:
	# @param A: tuple of integers
	# @param B: integers
	# @return a list of integers
	def searchRange(self, A, B):

		ans = [-1, -1]

		low = 0
		high = len(A) - 1

		while low <= high:
			mid = low + (high-low) // 2

			if A[mid] >= B:
				high = mid - 1
			if A[mid] < B:
				low = mid + 1

		if A[low] == B:
			ans[0] = low

		low = 0
		high = len(A) - 1

		while low <= high:
			mid = low + (high-low) // 2

			if A[mid] > B:
				high = mid - 1
			if A[mid] <= B:
				low = mid + 1

		if A[high] == B:
			ans[1] = high

		return ans





# Solution 2: 

from bisect import bisect_left, bisect_right
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        pos = bisect_left(A, B)
        pos2 = bisect_right(A, B) - 1
        if B != A[pos]:
            return [-1, -1]
        return [pos, pos2]