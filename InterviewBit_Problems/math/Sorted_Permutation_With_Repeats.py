# python 3 code

'''
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations.
Look at the example for more details.

Example :

Input : 'aba'
Output : 2

The order permutations with letters 'a', 'a', and 'b' : 
aab
aba
baa
The answer might not fit in an integer, so return your answer % 1000003

'''
#Import factorial from math module 
from math import factorial

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n=len(A)
        rank=1          #Initialize rank to 1
        
        #Loop to calculate number of smaller strings.
        for i in range(0,n):
            
            #Count smaller characters.
            less=0
            for j in range(i+1,n):
                if(A[i]>A[j]):
                    less+=1
            
            #Frequency of duplicate characters.
            l=[0]*52
            for k in range(i,n):
                if(A[k]>='A' and A[k]<='Z'):
                    l[ord(A[k])-ord('A')]+=1
                else:
                    l[ord(A[k])-ord('a')+26]+=1
            
            #Compute factorial of frequency of characters.
            fac=1
            for k in l:
                fac*=factorial(k)
                
            #Add possible number of smaller strings.    
            rank+=int((factorial(n-i-1)*less)/fac)
            
        return rank%1000003    
