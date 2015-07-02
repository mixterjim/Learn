def foo():
    r = open('0 Hello world.py')
    if r == (-1):
        return(-1)
    return r
def bar():
    r = foo()
    if r == (-1):
        print 'Error'  #BUG
    else:
        print 'OK'
bar()
