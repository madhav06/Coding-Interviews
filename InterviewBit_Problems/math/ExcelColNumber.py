# Python3

# Problem Description

# Given a column title A as appears in an Excel sheet, 
# return its corresponding column number.



# Problem Constraints
# 1 <= |A| <= 100



# Input Format
# First and only argument is string A.



# Output Format
# Return an integer

class Solution:

	# @param A: string
	# @return an integer
	def titleToNumber(self, A:
		result = 0

		for i in A:
			result = result * 26 + ord(i) - ord('A')+1
		return result