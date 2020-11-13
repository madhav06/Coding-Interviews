# Python3

# Given 2 non negative integers m and n, find gcd(m, n)

# GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
# Both m and n fit in a 32 bit signed integer.

# Example

# m : 6
# n : 9

# GCD(m, n) : 3 

class Solution:
	# @param A: integer
	# @param B: integer
	# return an integer
	def gcd(self, A, B):
		if B>A:
			A, B = B, A
		while B != 0:
			temp = B
			B = A%B
			A = temp

		return A