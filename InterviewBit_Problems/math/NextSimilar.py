# Python3

# Problem Description:
# Given a number A in a form of string
# You have to find the smallest numbers that has same set of digits as A and greater than A.

# If A is the greatest possible number with its set of digits, then return -1

# Constraints:

# 1 <= A <= 10 ** 100000

# # A doesn't contain leading zeros.

# Input First and Only argument is an numeric string denoting the number A

# Output: Return a string denoting the smallest number greater than A with same set of digits, 

class Solution:
	# @param A: string
	# @return a strings

	def solve(self, s):
		for i in range(len(s) - 2, -1, -1):
			tail = sorted(s[i:])
			for j in range(len(tail)):
				m = int(s[:i] + tail[j] + ''.join(tail[:j] + tail[j+1:]))

				if m > int(s):
					return m
		return '-1'