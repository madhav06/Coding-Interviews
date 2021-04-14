# python3 code
'''
Reverse the bits of an 32 bit unsigned int A

Constraints: 0 <= A <= 2 ^ 32

Input: First and only arg of input contains an integer A

Output: Return a single unsigned int, denoting decimal values of reverse bits

Input: 3
Output: 3221225472

'''

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ans=0
        for i in range(32) :
            if  A & 1<<i:
                ans=ans|(1<<(31-i))
               # print (ans)
        return ans  

