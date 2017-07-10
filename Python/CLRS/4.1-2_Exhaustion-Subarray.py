def EXHAUSTION_FIND_MAXIMUM_SUBARRAY(list):
    max = 0
    left = 0
    right = 0
    for i in range(0, len(list)):
        sum = list[i]
        for j in range(i, len(list)):
            if i == j:
                sum = list[j]
            else:
                sum += list[j]
            if sum > max:
                max = sum
                left = i
                right = j
    return left, right, max

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(EXHAUSTION_FIND_MAXIMUM_SUBARRAY(A))
