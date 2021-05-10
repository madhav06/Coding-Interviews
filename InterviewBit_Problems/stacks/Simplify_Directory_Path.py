# python3

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        dirs = A.split('/')
        result = []
        for c in dirs:
            if c == '' or c == '.': continue
            elif c == '..':
                if len(result)>0: result.pop()
            else:
                result.append(c)
        return '/'+'/'.join(result)