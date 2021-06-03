# python3

'''
Problem Description

1 <= |A| <= 2 * 10^5
1 <= A[i] <= 10 ^9

Input: First and only arg is array A

Output: Return one int, the answer to problem

Input: A [2, 4, 6]

output: 8

Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

Given an array A of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007.

'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        # All numbers have only 32 bits. Using this fact we can say 
        # if we can COUNT number of numbers with '1' at i-th bit, then
        # pairwise difference is (count * (len(A) - count) * 2)
        # Repeat operation for all 32 bits
        ans = 0  
      
        # traverse over all 32 bits 
        for i in range(32): 
          
            # count number of elements with i'th bit '1' 
            count = 0
            for j in A: 
                if ( (j & (1 << i)) ): 
                    count += 1
      
            # Add "count * (n - count) * 2" to the answer and take module
            ans += (count * (len(A) - count) * 2); 
            ans %= 1000000007
        return ans 
