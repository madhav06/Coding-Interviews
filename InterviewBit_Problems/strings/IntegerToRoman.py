# Given an integer A, convert it to a roman numeral, 
# and return a string corresponding to its roman numeral version

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        
        conversion = [ (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        out = ''
        
        for key, val in reversed(conversion):
            if A%key < A:
                num = A // key
                for i in range(num):
                    out = out + val
                A = A % key
        return out
