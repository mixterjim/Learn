def SELECTION_SORT(list):
    for n in range(0, len(list) - 1):
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
            return True
        if list[q + r] > value:
            p = p - r
        if list[q + r] < value:
            q = q + r
        r = int((p - q) / 2)
A = [1, 2, 5, 4, 3, 0, 6, 8, 9]
SELECTION_SORT(A)
v = int(input('Input:'))
k = 0
for i in range(0, len(A)):
    if BINARY_SEARCH(A, v - A[i]) != False:
        k = 1
        break
if k == 0:
    print(False)
else:
    print(True)
