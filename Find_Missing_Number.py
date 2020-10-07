# Python3
# Given a limited range array of size n where array contains element from 1 to n+1
# with one element missing, find that missing number without using extra space.

def findMissing(A):

	n = len(A)

	total = sum(A)

	return (n+1) + n*(n+1)//2 - total


if __name__ == '__main__':

	A = [3, 2, 5, 1]

	print("The missing element is", findMissing(A))


# time complexity = O(n), space complexity = O(1)

