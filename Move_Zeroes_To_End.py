# Python3

# function to move all the zeroes present in the list to the end
def reorder(A):

	# a variable to store index of next available position
	k = 0

	# if current element is non-zero, put element at next-free position in list
	for i in A:

		if i:
			A[k] = i
			k = k + 1

	# now moving zeroes to the end

	for i in range(k, len(A)):
		A[i] = 0

# moving all zeroes present in the list to the end

if __name__ == '__main__':

	A = [6, 0, 8, 2, 3, 0, 4, 0, 1]

	reorder(A)
	print(A)

# time complexity here will be O(n) and auxiliary space used will be O(1).