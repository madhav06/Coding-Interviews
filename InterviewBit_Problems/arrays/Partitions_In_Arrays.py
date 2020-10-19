#Python3

# Problem Description

# You are given a 1D integer array B containing A integers.

# Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

# Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])



# Problem Constraints
# 1 <= A <= 105

# -109 <= B[i] <= 109



# Input Format
# First argument is an integer A.

# Second argument is an 1D integer array B of size A.



# Output Format
# Return a single integer denoting the number of ways to split the array B into three parts with the same sum.



# Example Input
# Input 1:

#  A = 5
#  B = [1, 2, 3, 0, 3]

#  ANS: 3
# Input 2:

#  A = 4
#  B = [0, 1, -1, 0]

#  ANS: 0


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        x = sum(B)
        if x%3 !=0:
            return 0
        cur_sum = 0
        count  = 0
        total_count = 0
        x = x//3
        count = 0
        if x == 0:
            for i in range(A):
                cur_sum+= B[i]
                if cur_sum == x:
                    count+=1
                    total_count += max(0,count-2)
            return total_count    
        for i in range(A):
            cur_sum += B[i]
            if cur_sum == x:
                count+=1
            if cur_sum == 2*x and i!=0:
                total_count+= count
        return total_count 



 