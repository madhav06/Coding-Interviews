# Python 3

# Given a matrix of integers A of size N * M and an integer B.

# Write an efficient algo that searches for integer B in matrix A.

# Return 1 if B is present inA, else return 0.

def binarySearch(Arr, target):

	start = 0
	end = len(Arr)-1

	while start <= end:

		mid = (start + end) // 2

		if Arr[mid] == target:
			return mid

		elif Arr[mid] < target:
			start = mid + 1

		else:
			end = mid - 1

	return -1


class Solution:

	# @param A: list of list  of integers
	# @param B: integer
	# @return an integer

	def searchMatrix(self, A, B):

		start = 0

		end = len(Arr) - 1

		while start < end:

			mid = (start + end) // 2

			if A[mid][0] <= B:
				if B <= A[mid][-1]:

					start = mid
					break
				start = mid + 1
			else:

				end = mid - 1

		return 1 if binarySearch(A[start], B) != -1 else 0


		
			pass