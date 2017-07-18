A = [[1, 3], [7, 5]]
B = [[6, 8], [4, 2]]


def SQUARE_MATRIX_MULTIPLY(A, B):
    n = len(A)
    C = [[0] * n for x in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i][j] += A[i][k] * B[k][j]
    return C

print(SQUARE_MATRIX_MULTIPLY(A, B))
