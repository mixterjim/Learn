import random
import time
import copy


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
            INVERSION += q - p - i
    return INVERSION


def MERGE_SORT(list, p, r):
    global INVERSION
    INVERSION = 0
    if p < r - 1:
        q = int((r - p) / 2 + p)
        INVERSION += MERGE_SORT(list, p, q)
        INVERSION += MERGE_SORT(list, q, r)
        INVERSION += MERGE(list, p, q, r)
    return INVERSION

A = random_int_list(1, 100000, 10)

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
