class Solution:

    def findDiagonalOrder(self, matrix):
        result = []
        matrixRowSize = len(matrix)
        if matrixRowSize == 0:
            return result
        matrixColSize = len(matrix[0])
        returnSize = matrixRowSize * matrixColSize
        i = j = k = 0
        seq = 1
        if matrixRowSize == 1 or matrixColSize == 1:
            for i in range(matrixRowSize):
                for j in range(matrixColSize):
                    result.append(matrix[i][j])
                    k += 1
            return result
        while k < returnSize - 1:
            result.append(matrix[i][j])
            k += 1
            if i == matrixRowSize - 1:
                j += 1
            elif j == matrixColSize - 1:
                i += 1
            elif i == 0:
                j += 1
            elif j == 0:
                i += 1
            if seq == 1 and (i != matrixRowSize - 1 or j != matrixColSize - 1):
                while j != 0 and i != matrixRowSize - 1:
                    result.append(matrix[i][j])
                    k += 1
                    i += 1
                    j -= 1
            elif seq == -1 and (i != matrixRowSize - 1 or j != matrixColSize - 1):
                while i != 0 and j != matrixColSize - 1:
                    result.append(matrix[i][j])
                    k += 1
                    i -= 1
                    j += 1
            seq *= -1
        result.append(matrix[i][j])
        return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().findDiagonalOrder(matrix))
