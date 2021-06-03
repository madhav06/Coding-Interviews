# python3

# using collection
from collections import Counter

class Solution:
    def repeatedNumber(self, A):
        out = Counter(A)
        for i in out.keys():
            if out[i]>=2:
                return i
                
                
                
# best solution:
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n=len(A)
        seen=[False]*n
        for x in A:
            if seen[x]==True:
                return x
            else:
                seen[x]=True
        return -1