def CREATE_BINARY_LIST(list):
    num = input("Input binary number:")
    for n in range(0, len(num)):
        list.append(int(num[n]))


def GET_LIST_NUM(n, list):
    if n > len(list):
        return 0
    else:
        return list[-n]

A = []
B = []
CREATE_BINARY_LIST(A)
CREATE_BINARY_LIST(B)
n = max(len(A), len(B))
C = [0] * (n + 1)
for i in range(1, n + 1):
    C[-i] = GET_LIST_NUM(i, A) + GET_LIST_NUM(i, B) + C[-i]
    if C[-i] > 1:
        C[-i] -= 2
        C[-(i + 1)] += 1
print(C)
