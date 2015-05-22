import os
[d for d in os.listdir('.')]
'ABCDEFG'[:3]
'ABC'
'ABCDEFG'[::2]
'ACEG'
g = (x * x for x in range(10))
print g.next(),g.next(),g.next(),g.next()
for n in g:
    print n
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(6)
