def test():
    print 'Test'
t = test
print t.__name__
print '-----------------'
def log(function):
    def decorator(*args, **kw):
        print 'Name is %s():' %function.__name__
        return function(*args, **kw)
    return decorator
@log
def test():
    print 'Test'
test()
