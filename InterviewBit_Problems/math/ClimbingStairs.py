
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# Analysis: 

# It is not a hard question, especially if you finished the question: Unique Paths.


#simple, works, but exceed time limitation
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n==1: return 1
        if n==2: return 2
        res=[0 for i in range(n)]
        res[0]=1;res[1]=2;
        for i in range(2,n):
            res[i]=res[i-1]+res[i-2]
        return res[n-1]
test=Solution()
print(test.climbStairs(4))