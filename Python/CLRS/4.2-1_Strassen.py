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
        C[0][0] = A[0][0] * B[0][0]
    else:
        # C[0][0] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][0], B[0][0]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][1], B[1][0])
        # C[0][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][0], B[0][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0][1], B[1][1])
        # C[1][0] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0], B[0][0]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1], B[1][0])
        # C[1][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][0], B[0][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1], B[1][1])
        C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return C


def STRASSEN(A, B):
    S1 = B[0][1] - B[1][1]
    S2 = A[0][0] + A[0][1]
    S3 = A[1][0] + A[1][1]
    S4 = B[1][0] - B[0][0]
    S5 = A[0][0] + A[1][1]
    S6 = B[0][0] + B[1][1]
    S7 = A[0][1] - A[1][1]
    S8 = B[1][0] + B[1][1]
    S9 = A[0][0] - A[1][0]
    S10 = B[0][0] + B[0][1]
    P1 = A[0][0] * S1
    P2 = S2 * B[1][1]
    P3 = S3 * B[0][0]
    P4 = A[1][1] * S4
    P5 = S5 * S6
    P6 = S7 * S8
    P7 = S9 * S10
    n = len(A)
    C = [[0] * n for x in range(n)]
    C[0][0] = P5 + P4 - P2 + P6
    C[0][1] = P1 + P2
    C[1][0] = P3 + P4
    C[1][1] = P5 + P1 - P3 - P7
    return C

print(SQUARE_MATRIX_MULTIPLY(A, B))
print(SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B))
print(STRASSEN(A, B))
