# Python3

# Determine whether an integer is a palindrome. Do this without extra space.

# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# Negative numbers are not palindromic.

# Example :

# Input : 12121
# Output : True

# Input : 123
# Output : False

class Solution:
	# @param A: integer
	# @return an int

	def isPalindrome(self, A):

		reverse = 0
		num = A
		while num > 0:
			temp = num % 10
			reverse = reverse * 10 + temp
			num = math.floor ( num / 10 )

		if A == reverse:
			return 1
		else:
			return 0
