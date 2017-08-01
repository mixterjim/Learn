def MULTIPLY(a, b, c, d):
    A = (a + b) * (c + d)
    B = a * c
    C = b * d
    return B - C, A - B - C
print(MULTIPLY(1, 2, 3, 4))
