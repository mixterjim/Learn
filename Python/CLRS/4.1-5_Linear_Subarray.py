def LINEAR_SUBARRAY(list):
    low = 0
    max = 0
    for high in range(0, len(list)):
        if sum(list[low:high + 1]) > max:
            max = sum(list[low:high + 1])
            max_low = low
            max_high = high
        if sum(list[low:high + 1]) < 0:
            low = high + 1
        if list[high] > max:
            max = list[high]
            low = high
            max_low = low
            max_high = high
    return max_low, max_high, max

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(LINEAR_SUBARRAY(A))
