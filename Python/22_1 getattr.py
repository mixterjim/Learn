class Student(object):
    def __init__(self):
        self.name = 'Jack'
    def __getattr__(self,attr):
        if attr=='score':
            return 0
print 'Name:',Student().name
print 'Score:',Student().score

class Chain(object):
    def __init__(self, path):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print Chain().status.user.timeline.list
