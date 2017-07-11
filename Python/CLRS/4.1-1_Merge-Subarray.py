def FIND_MAX_CROSSING_SUBARRAY(list, low, mid, high):
    left_sum = -float('Inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + list[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -float('Inf')
    sum = 0
    max_right = mid
    for j in range(mid + 1, high):
        sum = sum + list[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def FIND_MAXIMUM_SUBARRAY(list, low, high):
    if high == low:
        return low, high, list[low - 1]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = FIND_MAXIMUM_SUBARRAY(list, low, mid)
        right_low, right_high, right_sum = FIND_MAXIMUM_SUBARRAY(list, mid + 1, high)
        cross_low, cross_high, cross_sum = FIND_MAX_CROSSING_SUBARRAY(list, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# A = [13, -3, -25, 20, -30, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
A = [100,5,-10,4]
print(FIND_MAXIMUM_SUBARRAY(A, 0, len(A)))
