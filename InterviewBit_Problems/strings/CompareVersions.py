# Python3

# Compare two version numbers version1 and version2.

# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.

class Solution:
    # @param A: String..
    # @param B: string..
    # @return an integer

    def compareVersion(self, A, B):
        ver_a = list(map(int, A.split('.')))
        ver_b = list(map(int, B.split('.')))

        for index in range(max(len(ver_a), len(ver_b))):

            a_num = ver_a[index] if index < len(ver_a) else 0
            b_num = ver_b[index] if index < len(ver_b) else 0

            if a_num < b_num:
                return -1
            elif a_num > b_num:
                return 1

        return 0

    




	   