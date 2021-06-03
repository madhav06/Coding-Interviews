# Python3

'''
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We return
X = 5

'''

def gcd(a, b):
    if b > a:
        b, a = a, b
    
    # 12, 6 ; 6, 0
    while b:
        a, b = b, a % b
    
    return a
    

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        ab_gcd = gcd(A, B)  # 2
        
        while ab_gcd > 1:
            A = A // ab_gcd  # 32    
            ab_gcd = gcd(A, ab_gcd)
            
        return A  # 16