
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A,):
        M, N = len(A), len(A[0])
        
        # let's figure out cost now
        cost = [[-1]*N for _ in range(M)]
        
        cost = [M-1][N-1] = A[M-1][N-1]
        
        return self.helper(0,0,A, cost)
        
        
        
    def helper(self, row, col, A, cost):
        M, N = len(A), len(A[0])
        if row == M or col == N:
            return float('inf')
        elif cost[row][col] != -1:
            return cost[row][col]
        
        else:
            right = self.helper(row, col+1, A, cost) 
            down = self.helper(row+1, col, A, cost)
            cost[row][col] = min(right, down)+ A[row][col] 
            return cost[row][col]
            
# check it, maybe let's see. 
    # what happened? 
//Sorry: TabError: inconsistent use of tabs and spaces in indentation (solution.py, line 17) 
# wait
