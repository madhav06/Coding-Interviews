# Maximum product of triplets (subseq of size 3)

# Given an integer array, find a maximum product of a triplet in a array.

# Input: [10,3,5,6,10]

# Output: 1200

import sys

# function to find a maximum product of a triplet in array of integers of size n
def maxProduct(arr, n):

	if n < 3:
		return -1

	max_product = -(sys.maxsize - 1)

	for i in range(0, n-2):
		for j in range(i+1, n-1):

			for k in range(j+1, n):

				max_product = max(
					max_product, arr[i]
					* arr[j] * arr[k])

	return max_product


# Driver Program

arr = [10,3,5,6,20]
n = len(arr)

max = maxProduct(arr,n)

if max == -1:
	print("NO Triplet Exists")
else:
	print("Maximum product is", max)

	