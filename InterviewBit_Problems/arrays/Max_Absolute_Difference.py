# Python3

# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        mx1= -2147483647
        mn1 = 2147483647
        mx2 = -2147483647
        mn2 = 2147483647
        
        for i in range(len(A)):
            # for equation 1
            mx1 = max(mx1, A[i]+i)
            mn1 = min(mn1, A[i]+i)
        
            # for equation 2
        
            mx2 = max(mx2, A[i]-i)
            mn2 = min(mn2, A[i]-i)
        
        return max(mx1-mn1, mx2-mn2)

    # Driver to test

    A = [-70, -64, -6, -56, 64, 61, -57, 16, 48, -98]

    print(maxArr(A))