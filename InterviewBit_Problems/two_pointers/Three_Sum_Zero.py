# Python 3 Code
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2) 
'''

class Solution:
    def threeSum(self, A):
        A.sort()
        answer, a = set(), None

        k, n = 0, len(A)

        for k in range(n - 2):
            a = A[k]
            i, j = k + 1, n - 1

            while i < j:
                sum_is = a + A[i] + A[j]
                if sum_is == 0:
                    answer.add((a, A[i], A[j]))
                    i , j = i + 1, j - 1
                elif sum_is < 0:
                    i += 1
                else:
                    j -= 1
        return list(answer)


if __name__ == "__main__":
    import time
    s = Solution()
    A = [0, 0, 0]
    print(len(A))

    print(s.threeSum(A))