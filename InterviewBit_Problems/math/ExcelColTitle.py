# Python3

# Problem Description

# Given a positive integer A, 
# return its corresponding column title as appear in an Excel sheet.



# Problem Constraints
# 1 <= A <= 1000000000



# Input Format
# First and only argument is integer A.



# Output Format
# Return a string, the answer to the problem.

class Solution:

	def convertToTitle(self, A):

		ans = ""

		while A != 0:
			k = A % 26

			if k != 0:
				 p = chr(k+64)
				 ans = ans + p
			else:

				ans = ans + 'Z'
				A = A - 1

			A = A // 26
		return (ans [::-1])



