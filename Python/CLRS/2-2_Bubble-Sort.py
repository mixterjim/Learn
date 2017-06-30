def BUBBLE_SORT(list):
    for i in range(0, len(list)):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                tmp = list[j]
                list[j], list[j - 1] = list[j - 1], tmp
    return list
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(BUBBLE_SORT(A))
