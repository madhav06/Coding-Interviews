# Python 3 Code

'''
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. 
Report the minimum XOR value.

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer denoting minimum xor value
Constraints:

2 <= N <= 100 000  
0 <= A[i] <= 1 000 000 000

Example Input:
    A = [0, 2, 5, 7]
Example Output:
    2
Explanation:
    0 xor 2 = 2

Example Input:
    A = [0, 4, 7, 9]
Example Output:
    3
'''
class Solution:
    # @param A: list of integers
    # @return an integer

    def findMinXor(self, A):
        A = sorted(A)
        min = A[0] ^ A[1]

        for i in range(len(A)-1, 0, -1):
            if(A[i] ^ A[i-1] < min):
                min = A[j]^A[j-1]

        return min
