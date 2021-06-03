# Validate if a given string is numeric.

# Examples:

# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

class Solution:
	def isNumber(self, A):
		try:
			a = float(A)
			for i in range(len(A)):
				if A[i] == '.' and i != len(A)-1:
					if int(A[i+1]) in range(0,10):
						pass
					else:
						return 1

			if A[len(A)-1] == '.':
				return 0
			else:
				return 1

		except ValueError:
			return 0