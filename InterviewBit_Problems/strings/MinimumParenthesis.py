# Python3

# Given a string A of parantheses ‘(‘ or ‘)’.

# The task is to find minimum number of parentheses ‘(‘ or ‘)’ (at any positions) we must add to make the resulting parentheses string valid.

# An string is valid if:

# Open brackets must be closed by the corresponding closing bracket.
# Open brackets must be closed in the correct order.


# Example Input
# Input 1:

#  A = "())"
# Input 2:

#  A = "((("


# Example Output
# Output 1:

#  1
# Output 2:

#  3


class Solution:
    # @param A: string
    # @return an integer
    def solve(self, A:
        stack = []
        for item in A:
            if item == '(':
                stack.append(item)
            else:
                if (len(stack) > 0 and stack[-1] == '(' ):
                    stack.pop()

                else:
                    stack.append(item)
                    
        return len(stack)