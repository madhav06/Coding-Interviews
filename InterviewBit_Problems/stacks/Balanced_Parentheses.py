# Problem Statement: Given a string A consisting only of '(' and ')'.

# You need to find whether parantheses in A is balanced or not ,
# if it is balanced then return 1 else return 0.

class Solution:
    #@param A: string
    #@return an integer
    def solve(self, A):
        stack = []
        closing = set( ')')
        for i in range(len(A)):
            if stack != []:
                last = stack.pop()
                if A[i] == ')':
                    if last != '(':
                        return 0
                    else:
                        stack.append(last)
                        stack.append(A[i])
                else:
                    if A[i] in closing:
                        return 0
                    else:
                        stack.append(A[i])
        
        if stack == []:
            return 1
        else:
            return 0
