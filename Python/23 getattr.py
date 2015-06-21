class Student(object):
    def __init__(self):
        self.name = 'Jack'
    def __getattr__(self,attr):
        if attr=='score':
            return 0
print 'Name:',Student().name
print 'Score:',Student().score
