# Given two numbers represented as strings, return multiplication of the numbers as a string.

#  Note: The numbers can be arbitrarily large and are non-negative.
# Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
# For example,
# given strings "12", "10", your answer should be “120”.

class Solution:

	def multiply(self, A, B):
		A = int(A)
		B = int(B)

		mul = str(A*B)
		return mul