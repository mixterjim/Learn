def SELECTION_SORT(list):
    for n in range(0, len(list)):
        tmp = list[n]
        for i in range(n, len(list) - 1):
            if tmp > list[i + 1]:
                tmp = list[i + 1]
                key = i + 1
                list[n], list[key] = list[key], list[n]

A = [489, 15, 89, 615, 89, 165, 6, 4, 65, 1]
SELECTION_SORT(A)
print(A)
