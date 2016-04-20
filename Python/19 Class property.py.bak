class Student(object):
    __slots__ = ('name', 'age', 'set_age')  #You can't use other property
Jim = Student()
Mirror = Student()
Jim.name = 'Jim'
Mirror.name = 'Mirror'
def set_age(self, age):
    self.age = age
from types import MethodType
Jim.set_age = MethodType(set_age, Jim)
Jim.set_age(20)
print Jim.age
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, Student)
Jim.set_score(100) #Assigned to Student.score
print 'Jim:',Jim.score
Mirror.set_score(1)
print 'Mirror:',Mirror.score
print Jim.score == Student.score
