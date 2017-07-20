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


def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B):
	n = len(A)
    C = [[0] * n for x in range(n)]
    if n == 1:
    	C[0][0] = A[0][0]*B[0][0]
    else:
    	C[0][0] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][0],B[0][0]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][1],B[1][0])
    	C[0][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][0],B[0][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][1],B[1][1])
    	C[1][0] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0],B[0][0]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1],B[1][0])
    	C[1][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0],B[0][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1],B[1][1])
    return C

print(SQUARE_MATRIX_MULTIPLY(A, B))
print(SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B))
