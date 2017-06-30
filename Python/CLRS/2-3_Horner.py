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


def HORNER(list, x):
    y = 0
    for i in range(len(list) - 1, -1, -1):
        y = list[i] + x * y
    return y


def NAIVE(list, x):
    y = 0
    for i in range(0, len(list)):
        y += list[i] * (x ** i)
    return y

x = 2
A = random_int_list(1, 100000, 1000)

B = A
start = time.clock()
HORNER(B, x)
end = time.clock()
print("Horner: %f s" % (end - start))

B = A
start = time.clock()
NAIVE(B, x)
end = time.clock()
print("Navie: %f s" % (end - start))
