# # Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.




# Input Format

# The only argument given is character array A.
# Output Format

# Return the value of arithmetic expression formed using reverse Polish Notation.

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        for i in A:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                right, left = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(left+right)
                if i == "-":
                    stack.append(left-right)
                if i == "*":
                    stack.append(left*right)
                if i == "/":
                    stack.append(int(float(left)/right))
        return stack.pop()