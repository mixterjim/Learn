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
