# python3

# Given a positive integer which fits in a 32 bit signed integer, 
# find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

# Example

# Input : 4
# Output : True  
# as 2^2 = 4.

class Solution:
	# @param A: integer
	# @return an integer

	def isPower(self, A):
		for pow in range(2, 33):
			num = round(A ** (1/pow))

			if (num ** pow == A):
				return 1
		return 0