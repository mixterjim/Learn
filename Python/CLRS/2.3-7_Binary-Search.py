def SELECTION_SORT(list):
    for n in range(0, len(list)):
        tmp = list[n]
        for i in range(n, len(list) - 1):
            if tmp > list[i + 1]:
                tmp = list[i + 1]
                key = i + 1
                list[n], list[key] = list[key], list[n]


def BINARY_SEARCH(list, value):
    q = 0
    p = len(list)
    r = int((p - q) / 2)
    while True:
        if len(list[q:p]) == 1 and list[q + r] != value:
            return False
        if list[q + r] == value:
            return q + r
        if list[q + r] > value:
            p = p - r
        if list[q + r] < value:
            q = q + r
        r = int((p - q) / 2)


def PLUS(list, v):
    for i in range(0, len(list)):
        tmp = BINARY_SEARCH(list, v - list[i])
        if tmp != False and tmp != i:
            return True
    return False

A = [1, 2, 5, 4, 3, 0, 6, 8, 9]
SELECTION_SORT(A)
v = int(input('Input:'))
print(PLUS(A, v))
