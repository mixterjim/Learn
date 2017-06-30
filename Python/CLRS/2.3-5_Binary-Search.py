# import random
# def random_int_list(start, stop, length):
#     start, stop = (int(start), int(stop)) if start <= stop else (
#         int(stop), int(start))
#     length = int(abs(length)) if length else 0
#     random_list = []
#     for i in range(length):
#         random_list.append(random.randint(start, stop))
#     return random_list


def CREATE_LIST(list):
    while True:
        key = input("Input:")
        if key == "":
            break
        list.append(int(key))


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
            return "NIL"
            break
        if list[q + r] == value:
            return q + r
            break
        if list[q + r] > value:
            p = p - r
        if list[q + r] < value:
            q = q + r
        r = int((p - q) / 2)
A = []
# A = [1, 2, 5, 4, 3, 0, 6, 8, 9]
# A = random_int_list(1, 100000, 100)
CREATE_LIST(A)
SELECTION_SORT(A)
print(A)
v = int(input("Find:"))
# for n in range(0, len(A)):
#     v = A[n]
print(BINARY_SEARCH(A, v))
