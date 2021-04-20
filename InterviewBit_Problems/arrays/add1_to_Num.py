# Given a non-negative number represented as an array of digits,

# add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# If the vector has [1, 2, 3]


# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        i = len(A) - 1
        add = 1

        while i >= 0:
            s = A[i] + add

            add = s // 10
            A[i] = s % 10
            i -= 1

            if not add:
                break
        else:
            A.insert(0, 1)

        while A and not A[0]:
            A.pop(0)

        return A

if __name__ == "__main__":
    A = [1, 2, 3]
    s = Solution()
    print(s.plusOne(A))
            
