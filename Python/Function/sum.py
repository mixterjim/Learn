l = []
for n in range(1, 101):
    l.append(n)
print(sum(l))


def fake_sum(x):
    s = 0
    for i in x:
        s = s + i
    return s
print(fake_sum(l))
