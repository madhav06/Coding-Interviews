# Python3:

# Find the contiguous subarray within an array, A of length N which has the largest sum.

# Input 1:
#     A = [1, 2, 3, 4, -10]

# Output 1:
#     10

# Explanation 1:
#     The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

# Input 2:
#     A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output 2:
#     6

# Explanation 2:
#     The subarray [4,-1,2,1] has the maximum possible sum of 6.

# This problem can be solved in optimal time by Kadane's Algorithm, which is a DP Approach: 
# local_maximum at index i is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.


# This way, at every index i, the problem boils down to finding the maximum of just two numbers, A[i] and (A[i] + local_maximum[i-1]). 
# Thus the maximum subarray problem can be solved by solving these sub-problems of finding local_maximums recursively.
#  Also, note that local_maximum[0] would be A[0] itself.
# Using the above method, we need to iterate through the array just once, which is a lot better than our previous brute force approach.
#  Or to be more precise, the time complexity of Kadane’s Algorithm is O(n)

# Kadane's Algo: finding the maximum of just two numbers, max(A[i] + local_maximum[i-1]). 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        local_max = global_max = A[0]
        
        # iterate through each index of array:
        for i in range(1,len(A)):
            local_max= max(A[i], (A[i] + local_max))
            
            if local_max > global_max:
                global_max = local_max
        
            #condition to check and update global max
        return global_max
