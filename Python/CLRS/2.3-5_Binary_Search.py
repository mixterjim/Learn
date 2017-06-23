def CREATE_LIST(list):
    while True:
        key = input("Input:")
        if key == "":
            break
        list.append(key)


def SELECTION_SORT(list):
    for n in range(0, len(list) - 1):
        tmp = list[n]
        for i in range(n, len(list) - 1):
            if tmp > list[i + 1]:
                tmp = list[i + 1]
                key = i + 1
                list[n], list[key] = list[key], list[n]


def BINARY_SEARCH(list, value):
    pass

A = [1, 2, 5, 4, 3, 0]
# CREATE_LIST(A)
SELECTION_SORT(A)
print(A)
v = input("Find:")
BINARY_SEARCH(A, v)
