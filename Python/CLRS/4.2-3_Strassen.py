import math


class STRASSEN:

    def __init__(self, A, B):
        n = len(A)
        if bin(n).count('1') > 1:
            k = 2**(int(math.sqrt(n)) + 1)
            l = [0] * k
            for i in range(k - n):
                A.append(l)
                B.append(l)
            for i in range(n):
                for j in range(k - n):
                    A[i].append(0)
                    B[i].append(0)
        C = self.Strassen(A, B)
        try:
            del(C[n:k])
            for m in range(n):
                del(C[m][n:])
        except:
            pass
        for i in range(0, len(C)):
            print(C[i])

    def Strassen(self, A, B):
        n = len(A)
        C = [[0] * n for i in range(n)]
        if n == 2:
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
            C[0][0] = P5 + P4 - P2 + P6
            C[0][1] = P1 + P2
            C[1][0] = P3 + P4
            C[1][1] = P5 + P1 - P3 - P7
            return C
        else:
            A1 = []
            A2 = []
            A3 = []
            A4 = []
            B1 = []
            B2 = []
            B3 = []
            B4 = []
            n = int(n / 2)
            for i in range(0, n):
                A1.append(A[0:n][i][0:n])
                A2.append(A[0:n][i][n:len(A)])
                A3.append(A[n:len(A)][i][0:n])
                A4.append(A[n:len(A)][i][n:len(A)])
            for i in range(0, n):
                B1.append(B[0:n][i][0:n])
                B2.append(B[0:n][i][n:len(B)])
                B3.append(B[n:len(B)][i][0:n])
                B4.append(B[n:len(B)][i][n:len(B)])
            P1 = self.Strassen(A1, self.Minus(B2, B4))
            P2 = self.Strassen(self.Plus(A1, A2), B4)
            P3 = self.Strassen(self.Plus(A3, A4), B1)
            P4 = self.Strassen(A4, self.Minus(B3, B1))
            P5 = self.Strassen(self.Plus(A1, A4), self.Plus(B1, B4))
            P6 = self.Strassen(self.Minus(A2, A4), self.Plus(B3, B4))
            P7 = self.Strassen(self.Minus(A1, A3), self.Plus(B1, B2))
            C1 = self.Plus(self.Minus(self.Plus(P5, P4), P2), P6)
            C2 = self.Plus(P1, P2)
            C3 = self.Plus(P3, P4)
            C4 = self.Minus(self.Minus(self.Plus(P5, P1), P3), P7)
            for i in range(0, n):
                C[i][0:n] = C1[i]
                C[i][n:len(A)] = C2[i]
                C[i + n][0:n] = C3[i]
                C[i + n][n:len(A)] = C4[i]
            return C

    def Plus(self, A, B):
        n = len(A)
        C = [[0] * n for i in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                C[i][j] = A[i][j] + B[i][j]
        return C

    def Minus(self, A, B):
        n = len(A)
        C = [[0] * n for i in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                C[i][j] = A[i][j] - B[i][j]
        return C

A = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
B = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

STRASSEN(A, B)
