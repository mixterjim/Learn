import random
import time
INVERSION = 0


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (
        int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def INVERSION_NUM(list):
    n = 0
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if i < j and list[i] > list[j]:
                n += 1
    return n


def MERGE(list, p, q, r):
    global INVERSION
    L = list[p:q]
    R = list[q:r]
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list[p] = L[i]
            i += 1
        else:
            list[p] = R[j]
            INVERSION += q + j - p
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
    return INVERSION

A = random_int_list(1, 10000, 100)
B = A[:]
start = time.clock()
print(MERGE_SORT(B, 0, len(B)))
end = time.clock()
print("MERGE: %f s" % (end - start))

B = A[:]
start = time.clock()
print(INVERSION_NUM(B))
end = time.clock()
print("INVERSION: %f s" % (end - start))
