# Python 3 Code

'''
Given an array S, of n integers, find three integers in S such that the sum is closest to a given number,target.
Return the sum of the three integers.

Example:

S = {-1, 2, 1, -4}
and target = 1

the sum that is c;osest to target is 2 (-1 + 2 + 1 = 2)
'''

class Solution:
    # @param A: list of ints
    # @param B: int
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        minn = float('INF')
        result = -1

        for i in range(0, len(A) - 2):
            a = A[i]
            start, end = i + 1, len(A) - 1

            while start < end:
                b, c = A[start], A[end]

                if abs(B - (a + b + c)) < minn:
                    minn = abs(B - (a + b + c))
                    result = a + b + c

                if a + b + c == B:
                    return B
                elif a + b + c > B:
                    end = end - 1
                else:
                    start = start + 1
        return result

if __name__ == "__main__":
    s = Solution()
    A = [-1, 2, 1, -4]
    print(s.threeSumClosest(A, 1))

