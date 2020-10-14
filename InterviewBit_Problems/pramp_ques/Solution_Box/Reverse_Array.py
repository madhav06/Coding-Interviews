# Python3

# Write a program to reverse an array or string



# Recursive:

	#Initialize start and end indexes as start = 0, end = n-1 
	#Swap arr[start] with arr[end] 
	#Recursively call reverse for rest of the array.

def reverseList(A, start, end):

	if start >= end:
		return
	A[start], A[end] = A[end], A[start]

	reverseList(A, start+1, end-1)


# testing 

A = [12, 23, 32, 45, 56, 61]
print(A)
reverseList(A, 0, 5)

reverseList("Reversed list is: ")
print(A)


# Time Complexity: O(n).
