class Student(object):
    __slots__ = ('name', 'age', 'set_age')  #Set property can use
    pass
s1 = Student()
s2 = Student()
s1.name = 'Jim'
s2.name = 'Mirror'
def set_age(self, age):
    self.age = age
from types import MethodType
s1.set_age = MethodType(set_age, s1)
s1.set_age(20)
print s1.age
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, Student)
s1.set_score(100)
print 'Jim:',s1.score
s2.set_score(0)
print 'Mirror:',s2.score
