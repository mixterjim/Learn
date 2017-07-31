class STRASSEN:

    def __init__(self, A, B):
        self.Size(A, B)
        n = len(A)
        if bin(n).count('1') > 1:
            k = 2**(len(bin(n)) - 2)
            l = [0] * k
            for i in range(k - n):
                A.append(l)
                B.append(l)
            for i in range(n):
                for j in range(k - n):
                    A[i].append(0)
                    B[i].append(0)
        C = self.Strassen(A, B)
        k = 0
        for i in range(1, len(C)):
            if C[-i].count(0) == len(C):
                k += 1
        n = len(C) - k
        del(C[n:])
        for m in range(n):
            del(C[m][n:])
        for i in range(len(C)):
            print(C[i])

    def Size(self, A, B):
        if len(A) < len(B):
            small, big = A, B
        elif len(A) > len(B):
            small, big = B, A
        else:
            return A, B
        if len(small) < len(big):
            for i in range(len(big)):
                for j in range(len(big) - len(small)):
                    big[i].append(0)
            for i in range(len(big) - len(small)):
                small.append([0] * len(big))
        return A, B

    def Strassen(self, A, B):
        n = len(A)
        tmp_n = 0
        C = [[0] * n for i in range(n)]
        for i in range(n):
            if A[i].count(0) == len(A):
                tmp_n += 1
        if tmp_n == n:
            return C
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
            for i in range(n):
                A1.append(A[0:n][i][0:n])
                A2.append(A[0:n][i][n:len(A)])
                A3.append(A[n:len(A)][i][0:n])
                A4.append(A[n:len(A)][i][n:len(A)])
            for i in range(n):
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
            for i in range(n):
                C[i][0:n] = C1[i]
                C[i][n:len(A)] = C2[i]
                C[i + n][0:n] = C3[i]
                C[i + n][n:len(A)] = C4[i]
            return C

    def Plus(self, A, B):
        n = len(A)
        C = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
        return C

    def Minus(self, A, B):
        n = len(A)
        C = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
        return C


A = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
B = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
STRASSEN(A, B)
