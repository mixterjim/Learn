import random
import time


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (
        int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def INSERTION_SORT(list, p, r):
    for n in range(p + 1, r):
        tmp = list[n]
        i = n - 1
        while i >= p and list[i] > tmp:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = tmp


def MERGE(list, p, q, r, k):
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


def MERGE_SORT(list, p, r, k):
    if len(list[p:r]) < k:
        INSERTION_SORT(list, p, r)
    elif p < r - 1:
        q = int((r - p) / 2 + p)
        MERGE_SORT(list, p, q, k)
        MERGE_SORT(list, q, r, k)
        MERGE(list, p, q, r, k)


A = random_int_list(1, 10000, 1000)

start = time.clock()
MERGE_SORT(A, 0, len(A), 20)
end = time.clock()
print("K=20 : %f s" % (end - start))

B = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
start = time.clock()
MERGE_SORT(A, 0, len(A), 0)
end = time.clock()
print("K= 0 : %f s" % (end - start))
