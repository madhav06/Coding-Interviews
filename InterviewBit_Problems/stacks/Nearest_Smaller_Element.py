# python3 Code here

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, array):
        """ Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        stack = []
        result = []
        for num in array:
            # see of there's integer smaller than num in the stack
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:  # found the smaller integer
                result.append(stack[-1])
            else:  # stack is empty, smaller integer wasn't found
                result.append(-1)
            stack.append(num)  # push current num to the stack
        return result