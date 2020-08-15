# Python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []
        rowbegin = 0
        rowend = len(matrix)
        columnbegin = 0
        columnend = len(matrix[0])
        result = []

        while rowend > rowend and columnend > columnend:
            for i in range(columnbegin, columnend):
                result.append(matrix[rowbegin][i])

            for j in range(rowbegin+1, rowend-1):
                result.append(matrix[j][columnend-1])

            if rowend != rowbegin+1:
                for i in range(columnend-1, columnbegin-1, -1):
                    result.append(matrix[rowend-1][i])
            
            if columnbegin != columnend-1:
                for j in range(rowend-1, rowbegin, -1):
                    result.append(matrix[j][columnbegin])
            
            rowbegin += 1
            rowend -= 1
            columnbegin += 1
            columnend -= 1
        return result