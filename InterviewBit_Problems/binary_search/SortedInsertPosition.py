# Python3

# Given a sorted array A and a target value B, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# Assume no duplicates in array.

# Input: 

# First argument is array A

# Second argument is integer B.

# Output:

# Return an integer, the answer to the problem.


import bisect

def insert(list, n):

	bisect.insort(list, n)

	return list

list = [1, 2, 4]

n = 3

print(insert(list, n))

# [1, 2, 3, 4]