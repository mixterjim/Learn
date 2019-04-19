class Solution:

    def spiralOrder(self, matrix):
        result = []
        matrixRowSize = len(matrix)
        if matrixRowSize == 0:
            return result
        matrixColSize = len(matrix[0])
        size = matrixRowSize * matrixColSize
        i = j = s = 0
        r = 1
        result.append(matrix[i][j])
        while(len(result) < size):
            s = int(r / 4)
            if r % 4 == 1:
                while j < matrixColSize - 1 - s:
                    j += 1
                    result.append(matrix[i][j])
            elif r % 4 == 2:
                while i < matrixRowSize - 1 - s:
                    i += 1
                    result.append(matrix[i][j])
            elif r % 4 == 3:
                while j > s:
                    j -= 1
                    result.append(matrix[i][j])
            elif r % 4 == 0:
                while i > s:
                    i -= 1
                    result.append(matrix[i][j])
            r += 1
        return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))
