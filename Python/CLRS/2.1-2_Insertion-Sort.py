def INSERTION_SORT(list):
    for n in range(1, len(list)):
        tmp = list[n]
        i = n - 1
        while i >= 0 and list[i] < tmp:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = tmp
    return list

A = [31, 41, 59, 26, 41, 58]
print(INSERTION_SORT(A))
