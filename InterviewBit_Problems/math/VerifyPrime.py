# Given a number N, verify if N is prime or not.

# Return 1 if N is prime, else return 0.

# Example :

# Input : 7
# Output : True

class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
	    
	    A = abs(A)
	    
	    # Special cases
	    if A == 1:
	        return 0
	    if A == 2:
	        return 1
	       
	    # If even (expect 2 itself), not prime.
	    if A % 2 == 0:
	        return 0
	        
	    # Try odd divisors.
	    # NB: we could optimize by trying prime divisors only.
	    for x in range(3, int(math.sqrt(A)) + 1, 2):
	        if A % x == 0:
	            return 0
	    return 1