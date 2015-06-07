def fib(n_max):
    n,a,b = 0,0,1
    while n < n_max:
        yield b
        a, b = b, a + b
        n = n + 1
list = fib(int(raw_input("Input a number:")))
print list.next()
for o in list:
    print o
