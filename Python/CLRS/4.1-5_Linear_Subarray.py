A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
A = [24123, -92062, 87140, -66200, 28729, -52079, 75847, -54146, -13648, -36461]


def LINEAR_SUBARRAY(list):
    low = 0
    max = 0
    for high in range(0, len(list)):
        if sum(list[low:high+1]) > max:
            max = sum(list[low:high+1])
            max_sum = max
            max_low = low
            max_high = high
        if sum(list[low:high+1]) < 0:
            max = 0
            low = high
        if list[high] > max_sum:
            max = list[high]
            low = high
            max_low = low
            max_sum = max
    return max_low, max_high, max_sum

print(LINEAR_SUBARRAY(A))
