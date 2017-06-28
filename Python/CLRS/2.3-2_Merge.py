def MERGE(list, p, q, r):
    L = list[p:q]
    R = list[q:r]
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list[p] = L[i]
            i += 1
        else:
            list[p] = R[j]
            j += 1
        p += 1
    if i > j:
        for j in range(j, len(R)):
            list[p] = R[j]
            p += 1
    else:
        for i in range(i, len(L)):
            list[p] = L[i]
            p += 1


def MERGE_SORT(list, p, r):
    if p < r - 1:
        q = int((r - p) / 2 + p)
        MERGE_SORT(list, p, q)
        MERGE_SORT(list, q, r)
        MERGE(list, p, q, r)

A = [3, 41, 52, 26, 38, 57, 9, 49]
MERGE_SORT(A, 0, len(A))
print(A)
