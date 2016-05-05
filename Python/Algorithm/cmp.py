# There is no cmp in Python 3
def cmp(x, y):
    if x - y < 0:
        return -1
    elif x > y:
        return 1
    return 0
print(cmp(1, 2), cmp(2, 1), cmp(1, 1))
