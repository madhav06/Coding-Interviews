
# Given a binary array, sort it in linear time and constant space, output should print: all zeros followed by all ones.

# we are going to use, partitioning logic of quicksort here.

# Function to sort
def sort(A):

	pivot = 1
	j = 0

	# each time we encounter 0, j is incremented and
	# 0 is placed before pivot

	for i in range(len(A)):
		if A[i] < pivot:

			swap(A, i, j)
			j = j+1

# function to swap two indices in the list

def swap(A,i,j):

	temp = A[i]
	A[i] = A[j]
	A[j] = temp

# Sort binary list in O(n)

if __name__ == '__main__':

	A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
	sort(A)

	# printnew list again
	print(A)