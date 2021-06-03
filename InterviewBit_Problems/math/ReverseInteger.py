# python3

# Reverse digits of an integer

# Example 1: x = 123, return 321

# Example 2: x = -123 return -321

# Return 0 if the result overflows and doesnot fit in 32 bit signed integer

class Solution:
	# @param A: integer
	# @return an integer

	def reverse(self, A):
		sign = -1 if A < 0 else 1
		A = abs(A)

		string = str(A)
		reverse = string[::-1]
		result = int(reverse)

		if result > 2**31 - 1:
			return 0
		return sign * result