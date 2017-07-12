import random
import time


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (
        int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


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
    for j in range(mid + 1, high + 1):
        sum = sum + list[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def FIND_MAXIMUM_SUBARRAY(list, low, high):
    if high == low:
        return low, high, list[low]
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


def FIND_MAXIMUM_SUBARRAY_HYBRID(list, low, high):
    if high == low:
        return low, high, list[low]
    elif len(list) < 50:
        return EXHAUSTION_FIND_MAXIMUM_SUBARRAY(list)
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


A = random_int_list(-100000, 100000, 1000)

start = time.clock()
print(EXHAUSTION_FIND_MAXIMUM_SUBARRAY(A))
end = time.clock()
print("EXHAUSTION_FIND_MAXIMUM_SUBARRAY: %f s" % (end - start))

start = time.clock()
print(FIND_MAXIMUM_SUBARRAY(A, 0, len(A)-1))
end = time.clock()
print("FIND_MAXIMUM_SUBARRAY: %f s" % (end - start))

start = time.clock()
print(FIND_MAXIMUM_SUBARRAY_HYBRID(A, 0, len(A)-1))
end = time.clock()
print("FIND_MAXIMUM_SUBARRAY_HYBRID: %f s" % (end - start))
