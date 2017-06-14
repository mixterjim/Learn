def MERGE(list, p, q, r):
    NaN = float('Inf')
    L = list[p:q]
    R = list[q:r]
    L.append(NaN)
    R.append(NaN)
    i = j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            list[k] = L[i]
            i = i + 1
        else:
            list[k] = R[j]
            j = j + 1


def MERGE_SORT(list, p, r):
    if p < r - 1:
        q = int((r - p) / 2 + p)
        MERGE_SORT(list, p, q)
        MERGE_SORT(list, q, r)
        MERGE(list, p, q, r)

A = [3, 41, 52, 26, 38, 57, 9, 49]
MERGE_SORT(A, 0, len(A))
print(A)
