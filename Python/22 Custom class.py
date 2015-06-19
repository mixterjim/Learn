class Student(object):
    def __init__(self, name):
        self.name = name
    #<__main__.Student object at 0x109afb190>
    def __str__(self):
        return self.name
    __repr__ = __str__    #get name in Variable
print(Student('Jim'))    
s = Student('Jim')  #Enter s get student name

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   #a=0 b=1
    def __iter__(self):
        return self     #return self and send to "__next__()"
    def next(self):     #"def __next__(self):" in Python 3.x
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration();  #exit loop
        return self.a
for n in Fib():
     print n

class Fib_s(object):
    def __getitem__(self, n):
        if isinstance(n, int): #index 'n'
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): #n is slice
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L
f = Fib_s()
print f[0:5]
