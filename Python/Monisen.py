# Formula M=2**P-1
import time
start = time.clock()
import math


def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True


def is_prime(n, k=32):
    prime_list = [2, 3]
    if n in (0, 1):
        return False
    if n in prime_list:
        return True
    if any((n % p) == 0 for p in prime_list):
        return False
    d, s = n - 1, 0
    return not any(try_composite(a, d, n, s)
                   for a in prime_list[:k])


def is_monisen(p):
    if is_prime(p) and is_prime(2**p-1):
        return True
    return False


def get_monisen(n):
    monisen = []
    num = 2
    while len(monisen) < n:
        if is_monisen(num):
            monisen.append(2**num-1)
        num += 1
    return monisen

n = 10  # Get Some Monisen
print("For the first %s Monisen numbers is:" % n, get_monisen(n))
end = time.clock()
print("Run: %f s" % (end - start))
