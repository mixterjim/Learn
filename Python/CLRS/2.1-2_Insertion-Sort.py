def INSERTION_SORT(list):
    for n in range(1, len(list)):
        for i in range(0, len(list) - 1):
            if list[i] < list[i + 1]:
                tmp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = tmp
    print(list)

A = [31, 41, 59, 26, 41, 58]
INSERTION_SORT(A)
