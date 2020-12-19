# Python3

# finding duplicate element from a limited range array
# Given a limited range array of size n where array contains elements between 1 to n-1 with one element repeating , find the duplicate number.

# Approach 1: Using Hash




# function to find duplicate
def findDuplicate(A):
	A = [1, 2, 5, 7, 7, 9]

	# creating a list visited, if element is seen before mark is visited
	visited = [False] * (len(A) + 1)

	for i in range(len(A)):

		# if element is seen before
		if visited[A[i]]:
			return A[i]

		# mark element as visited
		visited[A[i]] = True

	# when no duplicates found
	return -1

print("Duplicate element is", findDuplicate(A))
# if __name__ == '__main__':


	
