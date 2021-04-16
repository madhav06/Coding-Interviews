# Python 3 Code

'''
Problem Description

Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

Return the count modulo 109 + 7.



Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )modulo 109 + 7.

Input: A = 3
Output: 4

Input: A = 1
Output: 1
'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        n=A
        n+= 1
        powerOf2 = 2
        count = n // 2
        while (powerOf2 <= n):
            totalPairs = n // powerOf2
            count += (totalPairs // 2) * powerOf2
            if (totalPairs & 1) :
                count += (n % powerOf2)
            else :
                count += 0
            powerOf2 <<= 1
        return count%1000000007