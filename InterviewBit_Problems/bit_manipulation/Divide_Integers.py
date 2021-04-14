# Python 3 code

'''
Divide two ints without using multiplication, division, and mod operator

return floor of the result
'''

class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        return min(dividend // divisor, 2147483647)

