# Python 3 Code

class Solution:
	# @param A : string
	# @return a strings
	def reverseString(self, A):
        self.A = A
        A = A.next

        while A != 0:
            A = A.append()

            if A == A.len(A):
                break
            A.pop()

if __name__ == "__main__":

    A = 'abc'
    s = Solution()
    print(s.A)

