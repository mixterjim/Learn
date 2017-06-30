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


def INSERTION_SORT(list):
    for n in range(1, len(list)):
        tmp = list[n]
        i = n - 1
        while i >= 0 and list[i] > tmp:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = tmp


def SELECTION_SORT(list):
    for n in range(0, len(list)):
        tmp = list[n]
        for i in range(n, len(list) - 1):
            if tmp > list[i + 1]:
                tmp = list[i + 1]
                key = i + 1
                list[n], list[key] = list[key], list[n]


def MERGE(list, p, q, r):
    L = list[p:q]
    R = list[q:r]
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list[p] = L[i]
            i += 1
            p += 1
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


def BUBBLE_SORT(list):
    for i in range(0, len(list)):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                tmp = list[j]
                list[j], list[j - 1] = list[j - 1], tmp

A = random_int_list(1, 100000, 1000)

B = A
start = time.clock()
INSERTION_SORT(B)
end = time.clock()
print("INSERTION_SORT: %f s" % (end - start))

B = A
start = time.clock()
SELECTION_SORT(B)
end = time.clock()
print("SELECTION_SORT: %f s" % (end - start))

B = A
start = time.clock()
MERGE_SORT(B, 0, len(B))
end = time.clock()
print("MERGE_SORT: %f s" % (end - start))

B = A
start = time.clock()
BUBBLE_SORT(B)
end = time.clock()
print("BUBBLE_SORT: %f s" % (end - start))
