# python3

# Given an integer array A, find if an integer p exists in the array such that 
# the number of integers greater than p in the array equals to p.



# Input Format
# First and only argument is an integer array A.



# Output Format
# Return 1 if any such integer p is found else return -1

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    A.sort()  # sorting them first 
	    n = len(A)
	    for i in range(n-1):
	        if A[i] == A[i+1]:  # check occurances
	            continue
	        
	        if A[i] == n-i-1:   # any such integer found
	            return 1
	    
	    if A[n-1] == 0:   # if not found
	        return 1
	        
	    return -1