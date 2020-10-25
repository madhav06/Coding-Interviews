# python3

# Problem: 

# Given numRows, generate the first numRows of Pascal’s triangle.

# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

# Example:

# Given numRows = 5,

# Return

# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]


# We are handling every cases here.

# num at position i = number at position i in prev row + number at position (i + 1) in previous row.

class Solution(object):
    def solve(self, A):
        """
        :type A: int
        :rtype: List[List[int]]
        """
        if A == 1: return [[1]]
        res = []
        for i in range(A):
            if i == 0:
                res.append([1])
                continue
            tmp1 = res[i-1]
            tmp2 = [1]
            for j in range(len(tmp1)):
                if j == len(tmp1)-1:
                    tmp2 = tmp2+[tmp1[j]]
                    continue
                tmp2 = tmp2+[tmp1[j]+tmp1[j+1]]
            res.append(tmp2)
        return res

# Suggested solution here is:

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1,r):
                row.append(result[r-1][i-1] + result[r-1][i])
            row.append(1)
            result.append(row)
        return result